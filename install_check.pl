# install_check.pl

do 'mega-status-lib.pl';

# is_installed(mode)
# For mode 1, returns 2 if Apache is installed and configured for use by
# Webmin, 1 if installed but not configured, or 0 otherwise.
# For mode 0, returns 1 if installed, 0 if not
sub is_installed
{
return 0 if (!&has_command($config{'megaclisas'}));
return $_[0] ? 2 : 1;
}

