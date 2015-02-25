<!DOCTYPE html>
<html>
    <head>
        <title data-bind="text: title">$$PROG_NAME - $$PAGE_NAME</title>
	<link rel="icon" href="inc/images/favicon.png" type="image/png">
        <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
	<script type="text/javascript" src="lang/$$SERVER_LANG.js"></script>
   </head>
<body>

<div class="navbar">
  <div class="navbar-inner">
    <div class="container">
 
      <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
      <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </a>
 
      <!-- Be sure to leave the brand out there if you want it shown -->
      <a class="brand" href="#">$$PROG_NAME</a>
 
      <!-- Everything you want hidden at 940px or less, place within here -->
      <div class="nav-collapse collapse">
        <!-- .nav, .navbar-search, .navbar-form, etc -->
	<ul class="nav">
	<li>
	<a id="tab_scan_image"  class="pull-right"  href="index.cgi?page=scan">Scan Image</a>
	<script type="text/javascript">document.getElementById('tab_scan_image').innerHTML=lang_header.TAB_SCAN_IMAGE;</script>
	</li>

	<li>
	<a id="tab_recent_scans" href="index.cgi?page=scans">Recent Scans</a>
	<script type="text/javascript">document.getElementById('tab_recent_scans').innerHTML=lang_header.TAB_RECENT_SCANS;</script>
	</li>

	<li>
	<a id="tab_config" href="index.cgi?page=config"><i class="icon-wrench"></i>Configure</a>
	<script type="text/javascript">document.getElementById('tab_config').innerHTML=lang_header.TAB_CONFIGURE;</script>
	</li>
	</ul>
      </div>
 
    </div>
  </div>
</div>




<div class="container">
<div id="new_mes"></div>


<!--

	lenguaje
		<div id="language">
			<a href="index.cgi?page=$$PAGE&language=en_US" class="jack"><img src="inc/images/C-USA.jpg" alt="English (US)" title="Switch to English (US) interface"></a>
		</div>
		<div id="language">
			<a href="index.cgi?page=$$PAGE&language=zh_TW" class="jack"><img src="inc/images/C-Taiwan.jpg" alt="Traditional Chinese" title="Switch to Traditional Chinese interface"></a>
		</div>
-->

	<!--
		Linux Scanner Server
		written by PHiLLIP KLiEWER
		http://linuxscannerserver.sf.net
	-->

