#!/usr/bin/python

from matplotlib.backends.backend_svg import FigureCanvasSVG as FigureCanvas

from matplotlib.figure import Figure
import dateutil.parser
import sys
import io
import time, datetime
import CairoPlot
import cairo
import json
import string
import itertools
from contextlib import contextmanager
from pprint import pformat
from scikits import timeseries
import pandas
import pandas.io
import pandas.io.parsers

import logging
logging.basicConfig( stream=sys.stdout )
log = logging.getLogger( 'data.timseries.hacking' )
log.setLevel( logging.DEBUG )

log.debug( 'hello world' )
data = {}


class DefaultRecord( object ):
  __fields__ = [ 'date', 'time', 'reading' ]
  def __init__( self, header=[] ):
    self.header = header

  def decode( self, raw ):
    P       = map( string.strip, raw.split( ) )
    date    = dateutil.parser.parse( "T".join( P[ 0:2 ] ) )
    reading = P[ 2 ]

def RecordFactory( object ):
  def __init__( self, header ):
    self.header = header

  def decodeFields( self ):
    if self.header.startswith( '# ' ):
      if self.header[3:].split( ) == 3:
        pass


class InvalidRecord( Exception ): pass

@contextmanager
def data_stream( name='-' ):
  if name == '-':
    yield sys.stdin
  stream = open( name, 'r' )
  try:
    yield stream
  except InvalidRecord, e:
    log.error( 'error %r' % ( e ) )
    yield stream
  stream.close( )
  
def iter_data( stream ):
  for x, line in itertools.izip( itertools.count( ),
                                 stream.readlines( ) ):
    if line.startswith( '# ' ) is not True:
      yield line
  raise StopIteration( stream )

def get_data( stream ):
  # TODO: sensitivity to timezones!
  data  = {  }
  dates = [ ]
  for datum in iter_data( stream ):
    P = map( string.strip, datum.split( ) )
    try:
      date = dateutil.parser.parse( 'T'.join( 
                                    P[ 0:2 ] ) ) 
      dates.append( date )
      data[ date ] = int( P[ 2 ] )
      #data[ 'glucose' ].append( P[ 2 ] )
    except IndexError, e:
      log.error( 'error %s' % ( e ) )

  return dates, data

def get_pandas( name ):
  return pandas.io.parsers.parseText( stream )

def get_series( name ):
  data = None, None
  with data_stream( name ) as stream:
    data = get_data( stream )
  return data


if __name__ == '__main__':
  print "Generate a chart of a timeseries."
  data = [[3,4], [4,8], [5,3], [9,1]]

  index, data = get_series( sys.argv[ 1 ] )

  #dataList = list( data.values( ) )
  log.debug( pformat( data ) )
  #ts = timeseries.time_series( data.values( ), data.keys( ) )
  #log.debug( "##### scikits timeseries #####" )
  #log.debug( pformat( ts ) )


  log.debug( "##### pandas dump #####" )
  #drange = pandas.DateRange( data[ 'glucose' ] )
  ts = pandas.Series( data )
  log.debug( pformat( ts ) )
  log.debug( "##### index #####" )
  #log.debug( pformat( ts.index ) )
  log.debug( "##### values #####" )
  #log.debug( pformat( ts.values( ) ) )
  log.debug( "##### data #####" )
  #log.debug( pformat( ts.data ) )





  #xlim = [ 0,  10.0 ]
  #YMAX = ts.max( ) * 1.1
  #ylim = [ 0,  YMAX ]
  fig = Figure( )
  canvas = FigureCanvas(fig)
  #xticks = [ 1,2,3,4,5,6,7,8  ]
  #ax = fig.add_subplot(111, xlim=xlim, ylim=ylim,
  ax = fig.add_subplot(111)
  #data = [[False, False], [1,200],[4, 100],[6, 120]]
  #ax.plot(data)
  #D = dict( data )

  markers, stems, baselines, = ax.stem( ts.index, ts.values( ),
           linefmt='s-',
           markerfmt='ro',
           basefmt='b-' )
  fig.autofmt_xdate( )

  ax.set_title('glucose history')
  ax.grid(True)
  ax.set_xlabel('time')
  ax.set_ylabel('glucose')
  #fig.legend( stems, ts.index, 'top' )
  canvas.print_figure('test')

    

  

#####
# EOF
