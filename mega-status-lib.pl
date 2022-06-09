=head1 mega-status-lib.pl

Functions for getting SMART status

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
&init_config();
=head2 get_smart_version()

Returns the version number of the SMART tools on this system

=cut
sub get_mega_status
{
if (!defined($smartctl_version_cache)) {
	local $out = &backquote_command(
			"$config{'megaclisas'} 2>&1 </dev/null");
return $out;
    }
}


1;

