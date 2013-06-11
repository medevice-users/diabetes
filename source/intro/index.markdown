---
layout: page
title: "intro"
date: 2013-06-11 12:59
comments: true
sharing: true
footer: true
---

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


### [Projects](/intro/projects.html)

We need people of all stripes, from linux kernel hacking, to graphic
design.  We recognize that different types of people like to work on different types of projects, we've broken them down like this:

* [Visualizations](/intro/visualizations.html)
* [Firmware](/intro/firmware.html)
* [Hardware](/intro/hardware.html)
* [Backend](/intro/backend.html)
* [Vendor transports](/intro/vendors.html)
* [Math](/intro/math.html)
* [Device IO and decoder rings](/intro/devices.html)
* Web Development this site among others!
* [other projects](/intro/projects.html)
* [governance](/intro/governance.html)

