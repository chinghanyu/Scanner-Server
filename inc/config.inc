
<!-- Content -->

<div class="box">
	<h2><script type="text/javascript">document.write(lang_config.SCANNERS);</script></h2>
	<form name="scanner" action="index.cgi">
		<p>
			<script type="text/javascript">document.write(lang_config.SCANNERS_MSG);</script><br><br>
			<input type="hidden" name="page" value="config">
			<input type="submit" id="detect_btn" name="action" value="Search For Scanners">
			<script type="text/javascript">document.getElementById('detect_btn').value=lang_config.DETECT_BTN</script>
		</p>
	</form>
</div>

<div class="box">
	<h2><script type="text/javascript">document.write(lang_config.SANE_PKG_VER);</script></h2>
	<p>$$SANE_VER</p>
</div>

<div class="box">
	<h2><script type="text/javascript">document.write(lang_config.COLOR_SCHEME);</script></h2>
	<form name="color" action="index.cgi">
		<p>
			<script type="text/javascript">document.write(lang_config.SELECT_A_COLOR);</script>
			<input type="hidden" name="page" value="config">
			<input type="hidden" name="action" value="color">
			<select name="colors" onchange='this.form.submit()'>
				<option value="" selected="selected"> - - </option>
				<option id="colors_green" value="3c9642 3c7796" style="background-color:#3c9642;">Green</option>
				<option id="colors_blue" value="3c7796 963c8f" style="background-color:#3c7796;">Blue</option>
				<option id="colors_purple" value="963c8f 3c7796" style="background-color:#963c8f;">Purple</option>
				<option id="colors_black" value="000000 999999" style="background-color:#000000;">Black<</option>
				<option id="colors_gray" value="848484 bfbfbf" style="background-color:#848484;">Gray</option>
				<option id="colors_pink" value="ff007e bb045e" style="background-color:#ff007e;">Pink</option>
			</select>
			<script type="text/javascript">
				document.getElementById('colors_green').innerHTML=lang_config.COLOR_GREEN;
				document.getElementById('colors_blue').innerHTML=lang_config.COLOR_BLUE;
				document.getElementById('colors_purple').innerHTML=lang_config.COLOR_PURPLE;
				document.getElementById('colors_black').innerHTML=lang_config.COLOR_BLACK;
				document.getElementById('colors_gray').innerHTML=lang_config.COLOR_GRAY;
				document.getElementById('colors_pink').innerHTML=lang_config.COLOR_PINK;
			</script>
			<a onclick="window.location.reload()"><script type="text/javascript">document.write(lang_config.REFRESH);</script></a>
		</p>
	</form>
</div>

<div class="box">
	<h2><script type="text/javascript">document.write(lang_config.RECENT_SCANS);</script></h2>
	<p>
		<a href="index.cgi?page=scans&delete=Remove&file="><script type="text/javascript">document.write(lang_config.DELETE_ALL);</script></a>
	</p>
</div>

<!--
<div class="box">
<h2>Remove Saved Setting</h2>
<p>
$$SET_RESTORE
</p>
</div>
-->


