# Installation Instructions

The RSAL is designed to work on linux systems, and should work on most unixes.
For non-development work, either CentOS 6 or CentOS 7 are *strongly recommended*. Other versions and distributions should work, but you should know what you're doing.

- configure NFS mounts for `/public` (only needs to be accessable from the RSAL) and `/hold` (needs to be shared by RSAL and Dataverse).
- download RPM from the github [release page](https://github.com/sbgrid/rsal/releases)
- install RPM (and necessary dependencies). The EPEL repo is assumed to be available for these dependencies, but is not strictly required if you get the dependencies from elsewhere.
- install pip dependencies (`pip install -r /opt/rsal/scn/requirements.txt`)
- copy `/etc/dcm/lighttpd-conf-rsal` to `/etc/lighttpd/lighttpd.conf`, and edit if necessary (in particulary, to *restrict access to the Dataverse application server*).
- copy `/etc/dcm/lighttpd-modules-rsal` to `/etc/lighttpd/modules.conf`, and edit if necessary (which should only be necessary if you have installed in an unexpected manner).
- configure your rsync server appropriately for downloads.
- configure by (sigh) editing `/root/.bashrc` to set `DV_API_KEY`,`DV_HOST`.
- Start `lighttpd` service; create cron job to run `pub.py`.


These installation instructions are relatively recent, so please feel to open an issue in the [github repo](https://github.com/sbgrid/rsal/issues "RSAL github issues") if you find any problems or have suggestions.
