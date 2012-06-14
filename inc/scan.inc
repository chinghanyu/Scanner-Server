<!-- Content -->

<div id="sidebar">
	<form name="scanning" action="index.cgi">
		<!-- <input type="hidden" name="page" value="scan"> -->
		<!-- <input type="hidden" name="action" value="scan"> -->

		<div class="side_box">
			<h2><script type="text/javascript">document.write(lang_scan.SCANNERS);</script></h2>
			<p>
				<select name="scanner">
				$$SCANNERS
				</select>
			</p>
		</div>

		<div class="side_box">
			<h2><script type="text/javascript">document.write(lang_scan.SETTINGS);</script></h2>

			<div class="label"><script type="text/javascript">document.write(lang_scan.QUALITY);</script></div>
			<div class="control">
				<select name="quality">
					<option value="75">75 dpi</option>
					<option value="100">100 dpi</option>
					<option value="200" selected="selected">200 dpi</option>
					<option value="300">300 dpi</option>
					<option value="600">600 dpi</option>
					<option value="1200">1200 dpi</option>
				</select>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.SIZE);</script></div>
			<div class="control">
				<select name="size">
					<option id="size_full" value="full"></option>
					<option id="size_a4" value="210.0-297.0">A4</option>
					<option id="size_letter" value="215.9-279.4">Letter</option>
					<option id="size_4x6" value="101.6-152.4">4x6 Photos</option>
				</select>
				<script type="text/javascript">
					document.getElementById('size_full').innerHTML=lang_scan.SIZE_FULLPAGE;
					document.getElementById('size_a4').innerHTML=lang_scan.SIZE_A4;
					document.getElementById('size_letter').innerHTML=lang_scan.SIZE_LETTER;
					document.getElementById('size_4x6').innerHTML=lang_scan.SIZE_4X6;
				</script>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.ORIENTATION);</script></div>
			<div class="control">
				<select name="ornt">
					<option id="ornt_vert" value="vert">Portrait</option>
					<option id="ornt_horz" value="horz">Landscape</option>
				</select>
				<script type="text/javascript">
					document.getElementById('ornt_vert').innerHTML=lang_scan.ORIENTATION_PORTRAIT;
					document.getElementById('ornt_horz').innerHTML=lang_scan.ORIENTATION_LANDSCAPE;
				</script>
			</div>

		</div>

		<div class="side_box"><h2><script type="text/javascript">document.write(lang_scan.OUTPUT);</script></h2>

			<div class="label"><script type="text/javascript">document.write(lang_scan.MODE);</script></div>
			<div class="control">
				<select name="mode">
					<option id="mode_color" value="color">Color</option>
					<option id="mode_gray" value="gray">Gray</option>
					<option id="mode_lineart" value="lineart">Line Art</option>
				</select>
				<script type="text/javascript">
					document.getElementById('mode_color').innerHTML=lang_scan.MODE_COLOR;
					document.getElementById('mode_gray').innerHTML=lang_scan.MODE_GRAY;
					document.getElementById('mode_lineart').innerHTML=lang_scan.MODE_LINEART;
				</script>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.BRIGHT);</script></div>
			<div class="control">
				<select name="bright">
					<option value="-100">-100 %</option>
					<option value="-90">-90 %</option>
					<option value="-80">-80 %</option>
					<option value="-70">-70 %</option>
					<option value="-60">-60 %</option>
					<option value="-50">-50 %</option>
					<option value="-40">-40 %</option>
					<option value="-30">-30 %</option>
					<option value="-20">-20 %</option>
					<option value="-10">-10 %</option>
					<option value="0" selected="selected">0 %</option>
					<option value="10">+10 %</option>
					<option value="20">+20 %</option>
					<option value="30">+30 %</option>
					<option value="40">+40 %</option>
					<option value="50">+50 %</option>
					<option value="60">+60 %</option>
					<option value="70">+70 %</option>
					<option value="80">+80 %</option>
					<option value="90">+90 %</option>
					<option value="100">+100 %</option>
				</select>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.ROTATE);</script></div>
			<div class="control">
				<select name="rotate">
					<option id="rotate_0" value="0">0 deg</option>
					<option id="rotate_90" value="90">90 deg</option>
					<option id="rotate_180" value="180">180 deg</option>
					<option id="rotate_270" value="270">270 deg</option>
				</select>
				<script type="text/javascript">
					document.getElementById('rotate_0').innerHTML=lang_scan.ROTATE_0DEG;
					document.getElementById('rotate_90').innerHTML=lang_scan.ROTATE_90DEG;
					document.getElementById('rotate_180').innerHTML=lang_scan.ROTATE_180DEG;
					document.getElementById('rotate_270').innerHTML=lang_scan.ROTATE_270DEG;
				</script>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.SCALE);</script></div>
			<div class="control">
				<select name="scale">
					<option value="100"> 100 %</option>
					<option value="90">90 %</option>
					<option value="80">80 %</option>
					<option value="75"> 75 %</option>
					<option value="70">70 %</option>
					<option value="60">60 %</option>
					<option value="50"> 50 %</option>
					<option value="40">40 %</option>
					<option value="30">30 %</option>
					<option value="25"> 25 %</option>
					<option value="20">20 %</option>
					<option value="10">10 %</option>
				</select>
			</div>

			<div class="label"><script type="text/javascript">document.write(lang_scan.FILETYPE);</script></div>
			<div class="control">
				<select name="filetype">
					<option value="jpg">*.jpg</option>
					<option value="txt">*.txt</option>
					<option value="tiff">*.tiff</option>
					<option value="png">*.png</option>
				</select>
			</div>
		</div>

		<div class="side_box" style="text-align:center">
			<h2>
				<input type="submit" id="scan_btn" name="action" value="Scan Now" disabled>
				<script type="text/javascript">document.getElementById('scan_btn').value=lang_scan.SCAN_BTN</script>
			</h2>
		</div>

<!-- Save Settings -->
<!--
		<div class="side_box">
			<h2>Restore Settings</h2>
			<p></p>
		</div>
-->

		<div class="side_box"><h2><script type="text/javascript">document.write(lang_scan.SET_SAVE);</script></h2>
			<p>
				<input value="" name="set_save" size="15">
				<input type="submit" id="saveas_btn" name="saveas" value="Save">
				<script type="text/javascript">document.getElementById('saveas_btn').value=lang_scan.SAVE_AS_BTN</script>
			</p>
			<p>
				$$SET_RESTORE
			</p>
		</div>
	</form>
</div>		

<!-- Preview Pane -->
<div id="preview">
	<div id="preview_links">
		<h2><script type="text/javascript">document.write(lang_scan.PREVIEW_LINKS);</script></h2>
		<p>
			<img id="download_img" src="inc/images/download.png" alt="Download Image" title="Download image">
			<img id="print_img" src="inc/images/printer.png" alt="Print Image" title="Print image">
			<img id="delete_img" src="inc/images/delete.png" alt="Delete Image" title="Delete image">
		</p>
	</div>
	<script type="text/javascript">
		document.getElementById('download_img').title=lang_scan.DOWNLOAD_IMG;
		document.getElementById('print_img').title=lang_scan.PRINT_IMG;
		document.getElementById('delete_img').title=lang_scan.DELETE_IMG;
	</script>
	<div id="preview_image">
		<p>
			<img src="inc/images/preview.png" alt="Preview">
		</p>
	</div>
</div>
