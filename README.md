# x201-tablet-rotate-driver

A Python script that rotates and calibrates the ThinkPad X201 Tablet display with **xrandr** and **xsetwacom** in Linux Mint Cinnamon 19.

## Demo

<table>
</thead>
<tbody>
</tbody>
	<tr>
		<td width="140">
			Rotating Right (Portrait)
		</td>
		<td width="175">
			python3 driver.py -d -1
		</td>
		<td>
			<img src="./.github_readme/gif/rotate_right.gif" width="256"/>
		</td>
	</tr>
	<tr>
		<td>
			Rotating Left (Landscape)
		</td>
		<td>
			python3 driver.py -d -1
		</td>
		<td>
			<img src="./.github_readme/gif/rotate_left.gif" width="256"/>
		</td>
	</tr>
	<tr>
		<td>
			Rotating Left (Portrait)
		</td>
		<td>
			python3 driver.py -d -1
		</td>
		<td>
			<img src="./.github_readme/gif/rotate_left_again.gif" width="256"/>
		</td>
	</tr>
	<tr>
		<td>
			Automatic Calibration After Any Rotation
		</td>
		<td>
			GIF: after each rotation, the  display is calibrated to where the movement of the cursor due to the stylus and any finger presses is accurate and consistent.
		</td>
		<td>
			<img src="./.github_readme/gif/tracking.gif" width="256"/>
		</td>
	</tr>
</table>