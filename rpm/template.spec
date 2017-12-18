Name:           ros-indigo-actionlib
Version:        1.11.12
Release:        0%{?dist}
Summary:        ROS actionlib package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/actionlib
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rostest
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-std-msgs
Requires:       wxPython
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin >= 0.5.78
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rosnode
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 18 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Apr 06 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.7-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.6-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.11.3-0
- Autogenerated by Bloom

