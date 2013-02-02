
# Hacking diabetes

Fidelity of Care
################
Circa 2011
Despite many novel applications of technology to the
medical field, therapies for chronic disease lacks enough
transparency and credibility to humanely empower users to
manage therapy.


Diabetes Data Bus
=================
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

If you've created a visualization, add it to the list.  Include some sort of
self-attribution.

* http://jebeck.github.com/blog/2012/10/12/lessons-learned-from-100/
  Simply, excellent: love the heatmaps, and the classifications here
  Need ports to d3.js, or alteneratively [python?] daemon to serve results
  rendered by R.
* [iPancreas](https://github.com/jebeck/iPancreas)

* glucosurfer
* gists:
** [playing with time scales](https://gist.github.com/4292338)
** [glucose scatter with pan/zoom](https://gist.github.com/4265100)
** [hello world, glucose scatter](https://gist.github.com/4241973)

#### Firmware

For new devices, and to audit old devices.
* https://github.com/bewest/insulaudit/tree/master/hacking
  Includes pictures of working beaglebone, orchestrating the "data bus" between
  several connected devices, and the internet at large.

* [open embedded beaglebone firmware](https://github.com/n-west/meta-insulaudit)

* [open embed h8 stub](https://github.com/n-west/meta-h8) for giggles `;-)`

#### Hardware

List your hardware designs here.

#### Backend

Assume you have a bunch of decentralized "agents," implemented in many
languages, and all have data to report.

We'll need bits of the following types of software tailored for use by
a diabetic data bus:

If you've got software to keep records, allow read/write access to
them, add it to the list.

* asset management/inventory
* basic auditing/accounting/record keeping
* stats/data/mining
* authorization and authentication
* transport-independence - orchestrate which sockets, ports to use, etc.
** https://gist.github.com/4520642
** [netspective](https://github.com/netspective) may be of help

#### Vendor transports

Adapters for other web services:
glucosurfer, sugarstats, VISTA OSEHRA, INDIVO/SMART (CHIP), netspective,
others?

Also see ABBI: http://wiki.siframework.org/ABBI+Pull+Workgroup for
OAUTH based transport.

#### Math

Stats, predictive algorithms (so we can actually measure what we are
always implicitly predicting), the works.

If you've got a project that analyzes glucose, or insulin or similar
data, add it to the list:

* [DUBS](http://code.google.com/p/diabetes-understanding-by-simulation/)
  --  dubs is about understanding past and ongoing therapy by
  performing simulations to measure what were previously hidden and
  implicit expectations.

#### Device IO

The data on these devices belongs to us.  Let's get audit the data:
* [insulaudit](https://github.com/bewest/insulaudit)
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

#### Web Development

* gallery of visualizations, gist-based?
* gallery of advocacy, or maybe a "planet" style aggregator, with
  diabetesmine at the helm?
* docs, and technical writing
* templating for nice reports such as Jana's, we need to make it
  *easy* to produce documents to share like that.
