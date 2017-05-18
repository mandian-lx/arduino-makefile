%define oname Arduino-Makefile
%define lname %(echo %oname | tr [:upper:] [:lower:])

Summary:	Makefile for Arduino sketches
Name:		%{lname}
Version:	1.5.2
Release:	0
Group:		Sciences/Computer science
License:	LGPLv2.1+
URL:		https://github.com/sudar/Arduino-Makefile
Source0:	https://github.com/sudar/Arduino-Makefile/archive/%{version}/%{name}-%{version}.tar.gz
Buildarch: 	noarch

Requires:	config(arduino-core)
Requires:	python
Requires:	python3egg(pyserial)
Requires:	make

Suggests:	avrdude
Suggests:	cross-avr-gcc
Suggests:	cross-avr-gcc++

%description
This is a very simple Makefile which knows how to build Arduino sketches.

It defines entire workflows for compiling code, flashing it to Arduino and
even communicating through Serial monitor. You don't need to change anything
in the Arduino sketches.

Features:
  *  Very robust
  *  Highly customizable
  *  Supports all official AVR-based Arduino boards
  *  Supports chipKIT
  *  Supports Teensy 3.x (via Teensyduino)
  *  Works on all three major OS (Mac, Linux, Windows)
  *  Auto detects serial baud rate and libraries used
  *  Support for *.ino and *.pde sketches as well as raw *.c and *.cpp
  *  Support for Arduino Software versions 0.x, 1.0.x, 1.5.x and 1.6.x
     except 1.6.2. We recommend 1.6.3 or above version of Arduino IDE.
  *  Automatic dependency tracking. Referred libraries are automatically
     included in the build process. Changes in *.h files lead to
     recompilation of sources which include them

%files
%{_bindir}/ard-reset-arduino
%{_datadir}/arduino/arduino-mk-vars.md
%{_datadir}/arduino/*.mk
%{_mandir}/man1/ard-reset-arduino.1*
%docdir %{_docdir}/%{name}/examples
%doc README.md
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc licence.txt

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
	
%build
# Nothing to do here!

%install
# binaries
install -dm 0755 %{buildroot}/%{_bindir}/
install -pm 0755 bin/ard-reset-arduino %{buildroot}/%{_bindir}/

# data
install -dm 0755 %{buildroot}/%{_datadir}/arduino/
install -pm 0644 *.mk arduino-mk-vars.md %{buildroot}/%{_datadir}/arduino/

# manpage
install -dm 0755 %{buildroot}/%{_mandir}/man1/
install -pm 644 ard-reset-arduino.1 %{buildroot}/%{_mandir}/man1

# documentation
install -dm 0755 %{buildroot}/%{_docdir}/%{name}/
cp -far examples/ %{buildroot}/%{_docdir}/%{name}/

# remove .gitignore
find %{buildroot}/%{_docdir}/%{name}/ -name .gitignore -delete

