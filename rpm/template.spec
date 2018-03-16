Name:           ros-kinetic-actionlib
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS actionlib package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/actionlib
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-std-msgs
Requires:       wxPython
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin >= 0.5.78
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosnode
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-std-msgs

%description
The actionlib stack provides a standardized interface for interfacing with
preemptable tasks. Examples of this include moving the base to a target
location, performing a laser scan and returning the resulting point cloud,
detecting the handle of a door, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 16 2018 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Wed Jan 24 2018 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Nov 02 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Thu Mar 30 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Fri Feb 17 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.7-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.6-0
- Autogenerated by Bloom

* Mon Mar 14 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom
