# Hacking diabetes

Fidelity of Care
################
Circa 2011
Despite many novel applications of technology to the
medical field, therapies for chronic disease lacks enough
transparency and credibility to humanely empower users to
manage therapy.

## Insulaudit Agent
![insulaudit agent](https://raw.github.com/medevice-users/diabetes/master/3g-beagle-nextlink.JPG)
* [proxy modem: beaglebone + 3g modem + glucomter or insulin pump](https://github.com/bewest/insulaudit/tree/master/hacking)
* [securely proxy big data health services in the cloud](https://github.com/bewest/insulaudit-ssh-tools)
  Let's have a  market place auction for the best features, not for
  access, and not for safety.  The user always retains complete
  control over their devices, and their data.

## Diabetes Data Bus
There's a rising notion of a diabetes data bus.  A system
which integrates data collected from a variety of systems,
and communicates that data to authorized users.  In
addition, this infrastructure would support agents from an
expert systems presenting analyses and simulations of
expected results.

Diabetics own multiple mobile computers that record
biometric data on a regular basis.  This typically
includes a menagerie of glucometers, of which I own at
least 5, 2 of which are in active rotation at any given
time.  I also use an insulin pump, like many diabetics,
and it keeps logs of insulin given, as well as performs
opaque simulations on expected results.  In addition,
there are ancillary devices that measure interstitial
glucose levels on a real-time basis, as well as
pedometers, sleep monitors, and the list goes on ad
nauseum.

With so many sources of data critical to managing medical
therapy, it is impossible to predict the new sources of
data that will arise.  It's also impossible to replace all
the existing devices with new devices that are designed to
cooperate with one another.  However, all existing devices
have a serial port with which an authorized agent can
communicate with the device in order to audit therapeutic
details.  Therefore, it's much easier to adapt existing
devices into a common framework that knows how to present
data to expert systems, knows how to store data over time,
and knows how to keep the user connected to that data in
ways that allow better decision making.

Despite all the data currently logged by devices, how much
of it is leveraged to drive ongoing decisions?  The
proprietary software offered by medical industry offers
snapshots of interesting data from the past, and then asks
the user to manually fill in any missing data.  Each
manufacturer offers a perspective that their software
knows everything about managing diabetes, and in so doing
fails to offer a holistic perspective on therapy.

Instead, a data bus accepts input from a variety of
sources, aggregates it with other available sources, and
makes it available to the user at any time and any place.
The user can choose which applications can subscribe to
data, as well as re-route and transform data into those
applications.  Indivo already provides the container for
aggregating a user's data with customizable schema types.
Cube offers a great presentation engine for arbitrary
data.  When the two are tweaked to manage the data from
diabetic therapy, we have a diabetic data bus.


Many parts, loosely coupled.



## Help wanted

Join one of our mailing lists:

* [medevice](https://groups.google.com/forum/#!forum/medevice)
  For anyone wanting to increase the fidelity of their therapy using their
  skills and resources.  We have many projects, one of them probably your kind
  of project.

* [medical-device-users](https://groups.google.com/forum/#!forum/medical-device-users)
  Participate in developing advocacy to help share what and why we are doing.

* [insulaudit](https://groups.google.com/forum/#!forum/insulaudit) - for
  hacking insulaudit: discussion of python and features


### Projects

We need people of all stripes, from linux kernel hacking, to graphic
design.

#### Visualizations

Add your visualization here!
* [Flickr organized visual index](http://www.flickr.com/photos/dataviz/)

If you've created a visualization, add it to the list.  Include some sort of
self-attribution.

* http://jebeck.github.com/blog/2012/10/12/lessons-learned-from-100/
  Simply, excellent: love the heatmaps, and the classifications here
  Need ports to d3.js, or alteneratively [python?] daemon to serve results
  rendered by R.
* [iPancreas](https://github.com/jebeck/iPancreas)

* glucosurfer
* gists:

  * [playing with time scales](http://bl.ocks.org/4292338) [src](https://gist.github.com/4292338)
  * [glucose scatter with pan/zoom](http://bl.ocks.org/4265100) [src](https://gist.github.com/4265100)
  * [hello world, glucose scatter](http://bl.ocks.org/4241973) [src](https://gist.github.com/4241973)
  * [glucose heatmap](http://bl.ocks.org/bewest/5075497)
  * todo:
    * http://bl.ocks.org/mbostock/4736806
    * https://gist.github.com/bewest/4710009
    * http://bost.ocks.org/mike/cubism/intro/
    * (bad) [visualizing insulin](http://bl.ocks.org/bewest/5011908) [src](https://gist.github.com/bewest/5011908)
* http://ieg.ifs.tuwien.ac.at/projects/HorizonVis/
* http://www.cvast.tuwien.ac.at/projects/horizonvis
* diabetes_vis: [github rails src](https://github.com/benrudolph/diabetes_vis), [demo](http://diabetesvis.herokuapp.com/diabetes/dashboard)
* http://ciid.dk/education/portfolio/idp12/courses/data-visualisation/projects/blood-sugar-visualization/
* 

#### Firmware

For new devices, and to audit old devices.
* [proxy modem: beaglebone + 3g modem + glucomter or insulin pump](https://github.com/bewest/insulaudit/tree/master/hacking)
  Includes pictures of working beaglebone, orchestrating the "data bus" between
  several connected devices, and the internet at large.
* [insulware](https://github.com/n-west/insulware) - mash up
  beaglebone, meta-insulaudit, and insulaudit altogether in one
  package to audit gucometers over the internet using 3G!
* [registration scripts](https://github.com/ehwest/cloudify) - demo
  app to send SMS messages for registered users to [insulware]
* [insulaudit in the cloud](https://github.com/bewest/insulaudit-ssh-tools)
  Considering extending gitolite.  ssh based application that
  sets up a transport, then uses insulaudit or related tools.

* [open embedded beaglebone firmware](https://github.com/n-west/meta-insulaudit)

* [open embed h8 stub](https://github.com/n-west/meta-h8) for giggles `;-)`

#### Hardware

List your hardware designs here.
Reference designs for pumps, sensors, meters, connectors, etc...
* http://www.ncbi.nlm.nih.gov/pubmed/22226258
* http://www.ti.com/product/rm48l950
* [reference infusion pump design](http://www.ti.com/solution/infusion_pump)
* [reference meter design](http://www.ti.com/solution/medical_meters_portable)
* http://www.cooking-hacks.com/index.php/ehealth-sensors-complete-kit-biometric-medical-arduino-raspberry-pi.html

#### Backend

Assume you have a bunch of decentralized "agents," implemented in many
languages, and all have data to report.

We'll need bits of the following types of software tailored for use by
a diabetic data bus:

If you've got software to keep records, allow read/write access to
them, add it to the list.

* asset management/inventory
* basic auditing/accounting/record keeping

  * [opendatabetes](http://opendatabetes.com) - an open standard for recording/sharing diabetes data - very early days 
  * [sanguine](http://sanguinediabetes.com) - WIP glucose/insulin/pump tracking app. In prototype, to be rebuilt using web technologies

* stats/data/mining
* authorization and authentication
* transport-independence - orchestrate which sockets, ports to use, etc.

  * https://gist.github.com/4520642
  * [netspective](https://github.com/netspective) may be of help

* [manageBGL](http://manageBGL.com) pump simulator and data visualization with API


#### Vendor transports

Bus consumers.

Adapters for other web services:
glucosurfer, sugarstats, VISTA OSEHRA, INDIVO/SMART (CHIP), [@netspective],
others?

Also see ABBI: http://wiki.siframework.org/ABBI+Pull+Workgroup for
OAUTH based transport.

* [connect](https://github.com/CONNECT-Solution/CONNECT)
* [Sanguine](http://sanguinediabetes.com) is an app already "in the wild", it
should be able to either poll one of our compatible servers and fetch/store
medical records and annotations.
* [opendatabetes](http://opendatabetes.com) - an open standard for recording/sharing diabetes data - very early days 
* [indivo](http://docs.indivohealth.org/en/v2.0.0/schemas/index.html) python/django friendly


#### Math

Stats, predictive algorithms (so we can actually measure what we are
always implicitly predicting), the works.

If you've got a project that analyzes glucose, or insulin or similar
data, add it to the list:

* [DUBS](http://code.google.com/p/diabetes-understanding-by-simulation/)
  --  dubs is about understanding past and ongoing therapy by
  performing simulations to measure what were previously hidden and
  implicit expectations.
* http://www.ncbi.nlm.nih.gov/pubmed/10994512
* http://www.2aida.net/welcome/
* http://www.ncbi.nlm.nih.gov/pubmed?itool=pubmed_Abstract&DbFrom=pubmed&Cmd=Link&LinkName=pubmed_pubmed&IdsFromResult=9183777&retmode=ref
* http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3320833/
* http://www.2aida.org/aida/research2.htm
* http://oucsace.cs.ohiou.edu/~marling/smarthealth/projects.html
* 

#### Device IO

The data on these devices belongs to us.  Let's get audit the data:
* [insulaudit](https://github.com/bewest/insulaudit) - this project consumes many libraries to re-format data in a prefered format

##### Decoder rings
These projects collect packet captures, provide tests suites, and tools to
communicate with medical devices.  Application authors can use these
tools to analyze and debug devices, exercise their decoding skills, or
contribute to language-independent test suites, or even help implement
the protocols.

* [decoding-carelink](https://github.com/bewest/decoding-carelink)
* [decoding-omnipod](https://github.com/bewest/decoding-omnipod)
* [decoding-onetouchping](https://github.com/bewest/decoding-onetouchping)
* [decoding-dexcom](https://github.com/bewest/decoding-dexcom)
* [decoding-bayer](https://gist.github.com/4696755)
* [glucodump](https://bitbucket.org/iko/glucodump/src/e37ea2a38776/glucodump/usbcomm.py)

Unit tests, docs, protocol schematics, ports to other languages.

Help with the "decoder rings," some have data available, ready to
analyze, some need captures!

#### Git based medical record?

Would solve transport and versioning issues.
* `git-phr` - if only!

#### Web Development

* gallery of visualizations, gist-based? *proposed*:
```
databetics.com/ -> here (medevice/diabetes)
databetics.com/visual/ -> here (medevice/diabetes/visual)
databetics.com/formats/ -> damon's databetes?
databetics.com/projects/ -> better list of projects we actually commit on
short term projects:
  iPancreas: re-usable, blog-posting tool
  visualizations: need to make it easy for more people to make
    graphs and charts, to iterate on UI, etc... this is essentially UI
    development broken down, feature by feature
  insulaudit: pumping data out so that sanguine, ipancreas and others
              can consume, pushing support for more devices,
              implementing in other languages?
```
* gallery of advocacy, or maybe a "planet" style aggregator, with
  diabetesmine at the helm?
* docs, and technical writing
* templating for nice reports such as Jana's, we need to make it
  *easy* to produce documents to share like that.

#### other projects

Mostly personal loggers.

* apple https://github.com/kamexy/GlucoseLogger
* apple https://github.com/mstoth/GlucoseReader
* https://github.com/gandalfn/glucose-board
* java https://github.com/jccgit/GlucoseTracker
* [model of insulin and glucose](https://github.com/JohnCarlosReed/GlInGgModel)
* https://github.com/yasminlucero/HBG
* https://github.com/njonsson/glucodes
* https://github.com/diminish7/glucotracker
* MS https://github.com/kmoormann/ScarlettsDiabetesMobileLog
* https://github.com/Firebright/Diabetes_data_analysis
* https://github.com/techniker/OpenAvivaIRCom
* https://github.com/pikesley/insulin
* https://github.com/graham1034/Smith2012_insulin_signalling
* https://github.com/damondouglas/yale_insulin_algorithm
* https://github.com/BrendanLeber/Doser
* https://github.com/nielubowicz/iAbetes
* https://github.com/pnbloem/DiabetesTracker
* https://github.com/alexpeachey/digital-pancreas
* https://github.com/kmoormann/Paulescu
* https://github.com/rlaskey/dm-track
* https://github.com/gitpan/Palm-DiabetesPilot
* https://github.com/david-hathaway/BolusCalculator
* https://github.com/Sushisugre/Glucose/tree/master/src/cn/edu/tongji/sse/glucosemeter
* https://github.com/cubabit/WebService-GlucoseBuddy
* iphone app https://github.com/bslayton/glu-iphone
* python https://github.com/onelson/mreader
* rails https://github.com/HaKr/diabetesdiary
* python... https://github.com/onelson/mreader
* linux/gtk https://github.com/flupzor/glucosemeter
* MS web app https://github.com/healthmonitor/HealthMonitoringSystem
* rails https://github.com/HaKr/diabetesdiary
* rails https://github.com/flugsio/rails-glucosejournal
* android https://github.com/flugsio/android-glucosejournal
* https://github.com/antonio/ontrack-pretty-reports
* https://github.com/TwelveBaud/diabot-plugins
* accucheck schematics https://github.com/techniker/OpenACCPplus
* schematics https://github.com/techniker/OpenWeCalla
* formatting https://github.com/nezt/hl72xml/blob/master/python_src/sendHL7.py
* SMART App https://github.com/arjunsanyal/smart_hv_merge_app
* "TCL is a great language for processing HL7 messages" https://github.com/jamerfort/tclhl7
* 



## Documentation
* documenting what we've done for the FDA/creating a suite of IP-free technology requires documentation!
  * http://www.ncbi.nlm.nih.gov/pubmed/22226258
  * http://www.w3.org/Consortium/Patent-Policy-20040205/
  * http://tools.ietf.org/html/draft-morton-ippm-advance-metrics-02
  * http://www.ncbi.nlm.nih.gov/pubmed/20307387
  * http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2864162/
  * http://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/GeneralHospitalDevicesandSupplies/InfusionPumps/ucm202511.htm
  * http://www.fda.gov/medicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/ucm206153.htm
  * http://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/HomeHealthandConsumer/ConsumerProducts/ArtificialPancreas/ucm259555.htm

=======
# split
## What is Octopress?

Octopress is [Jekyll](https://github.com/mojombo/jekyll) blogging at its finest.

1. **Octopress sports a clean responsive theme** written in semantic HTML5, focused on readability and friendliness toward mobile devices.
2. **Code blogging is easy and beautiful.** Embed code (with [Solarized](http://ethanschoonover.com/solarized) styling) in your posts from gists, jsFiddle or from your filesystem.
3. **Third party integration is simple** with built-in support for Pinboard, Delicious, GitHub Repositories, Disqus Comments and Google Analytics.
4. **It's easy to use.** A collection of rake tasks simplifies development and makes deploying a cinch.
5. **Ships with great plug-ins** some original and others from the Jekyll community &mdash; tested and improved.


## Documentation

Check out [Octopress.org](http://octopress.org/docs) for guides and documentation.


## Contributing

[![Build Status](https://travis-ci.org/imathis/octopress.png?branch=master)](https://travis-ci.org/imathis/octopress)

We love to see people contributing to Octopress, whether it's a bug report, feature suggestion or a pull request. At the moment, we try to keep the core slick and lean, focusing on basic blogging needs, so some of your suggestions might not find their way into Octopress. For those ideas, we started a [list of 3rd party plug-ins](https://github.com/imathis/octopress/wiki/3rd-party-plugins), where you can link your own Octopress plug-in repositories. For the future, we're thinking about ways to easier add them them into our main releases.


## License
(The MIT License)

Copyright © 2009-2013 Brandon Mathis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ‘Software’), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ‘AS IS’, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#### If you want to be awesome.
- Proudly display the 'Powered by Octopress' credit in the footer.
- Add your site to the Wiki so we can watch the community grow.
