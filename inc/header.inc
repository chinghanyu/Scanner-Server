<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>

<!--

Linux Scanner Server
written by PHiLLIP KLiEWER
http://linuxscannerserver.sf.net

-->

	<title>BCCL | $$PROG_NAME - $$PAGE_NAME</title>
	<link rel="stylesheet" href="config/style.css" type="text/css">
	<link rel="shortcut icon" href="inc/images/favicon.ico" type="images/x-icon">
	<link rel="icon" href="inc/images/favicon.png" type="image/png">
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8">
	<script type="text/javascript" src="lang/$$SERVER_LANG.js"></script>
</head>

<body>
<div id="container">

	<div id="header">

		<div id="logo">
			<img src="inc/images/logo.png" alt="Scanner Server">
		</div>
		
		<div id="language">
			<a href="index.cgi?page=$$PAGE&language=en_US" class="jack"><img src="inc/images/C-USA.jpg" alt="English (US)" title="Switch to English (US) interface"></a>
		</div>
		<div id="language">
			<a href="index.cgi?page=$$PAGE&language=zh_TW" class="jack"><img src="inc/images/C-Taiwan.jpg" alt="Traditional Chinese" title="Switch to Traditional Chinese interface"></a>
		</div>
		
		<div class="tab">
			<a id="tab_config" href="index.cgi?page=config">Configure</a>
			<script type="text/javascript">document.getElementById('tab_config').innerHTML=lang_header.TAB_CONFIGURE;</script>
		</div>
		<div class="tab">
			<a id="tab_recent_scans" href="index.cgi?page=scans">Recent Scans</a>
			<script type="text/javascript">document.getElementById('tab_recent_scans').innerHTML=lang_header.TAB_RECENT_SCANS;</script>
		</div>
		<div class="tab">
			<a id="tab_scan_image" href="index.cgi?page=scan">Scan Image</a>
			<script type="text/javascript">document.getElementById('tab_scan_image').innerHTML=lang_header.TAB_SCAN_IMAGE;</script>
		</div>
		<div class="tab">
			<a href="http://$$SERVER_URL">$$SERVER_NAME</a>
		</div>

	</div>

	<noscript>
		<div id="message">
			<h2>JavaScript Disabled</h2>
			<p>This application requires JavaScript to function. Please enable JavaScript, then reload this page</p>
		</div>
	</noscript>

	<div id="new_mes">
	</div>
