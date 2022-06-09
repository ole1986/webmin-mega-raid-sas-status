#!/usr/bin/perl
# Show all drives and their SMART status

require './mega-status-lib.pl';
&ReadParse();

# Make sure MEGA commands are installed
if (!&has_command($config{'megaclisas'})) {
	&ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);
	&ui_print_endpage(
		&ui_config_link('index_ecmd',
		        [ "<tt>$config{'megaclisas'}</tt>", undef ]));
	}

# Show the version
$ver = &get_mega_status();
if (!$ver) {
	&ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);
	&ui_print_endpage(
		&ui_config_link('index_ecmd2',
		        [ "<tt>$config{'megaclisas'}</tt>", undef ]));
	}

&ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1, 0,
		 &help_search_link("megaclisas", "man", "doc", "google"),
		 undef, undef,
		 undef);

($raid, $model) = ($ver =~ /([a-z][0-9]+) \| (.*)/i);


@m = split /\n/s, $ver;

print "<div style='float:left;font-weight:bold;'>". &text('index_model', $model)."</div>";

$gStatus = "<span style='color: #04B304'>Optimal</span>";

for my $el (@m) {
    ($id, $type, $size, $status, $prog) = ($el =~ /^([a-z][0-9][a-z][0-9]) \| (.*?) \| (.*?) \| (.*?) \| (.*?)$/si);
    if($status ne "" && $status ne "Optimal") {
	$gStatus = "<span style='color:red;'>$status</span>";
	last;
    }
}
print "<div style='float:right;font-weight: bold;'>STATUS: $gStatus</div>";

print "<div style='clear:both;'>&nbsp;</div>";
print "<div style='margin-bottom: 1em;'>Details:</div>";
print "<pre>$ver</pre>";
