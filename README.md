# x201-tablet-rotate-driver

A Python script that rotates and calibrates the ThinkPad X201 Tablet display with **xrandr** and **xsetwacom** in Linux Mint Cinnamon 19.

## Setup and Use
Since it supports command-line arguments, the script can be used manually in the terminal:

To rotate the display 90 degrees counter-clockwise to the "left," run
```
python3 driver.py -d 1
```
which is the same as running the script without any arguments
```
python3 driver.py
```

To rotate the display 90 degrees clockwise to the "right," run
```
python3 driver.py -d -1
```

However, it is much more ideal and efficient to execute the command through a touchscreen-friendly widget:

<table>
</thead>
<tbody>
</tbody>
	<tr>
		<td width="256">
			In my particular setup, I used two "Command Launcher" widgets: one to rotate clockwise, another to rotate counterclockwise. Command-executing widgets should be available in many other desktop environments such as XFCE, KDE, or MATE, to name a few.
		</td>
		<td>
			<img src="./.github_readme/still/widget_closeup.jpg" width="256"/>
		</td>
	</tr>
	<tr>
		<td>
			To configure the widgets in Cinnamon, simply right click one and click on "Configure..."
		</td>
		<td>
			<img src="./.github_readme/still/widget_closeup_menu.jpg" width="256"/>
		</td>
	</tr>
	<tr>
		<td>
			At a minimum, update the "command" field of the left and right widgets:
		<table>
		</thead>
		<tbody>
		</tbody>
			<tr>
				<td>
					LEFT
				</td>
				<td>
					python3 PATH -d 1
				</td>
				</tr>
			<tr>
				<td>
					RIGHT
				</td>
				<td>
					python3 PATH -d -1
				</td>
			</tr>
		</table>
			Where "PATH" is the ABSOLUTE path to the driver.py file (relative paths are not recommended here). The script does NOT need to be ran as root. You may also optionally adjust the widget icon, keyboard shortcut, notification, etc.
		</td>
		<td>
			<img src="./.github_readme/still/widget_command_edit.jpg" width="256"/>
		</td>
	</tr>
</table>


## Demo with Widget

<table>
</thead>
<tbody>
</tbody>
	<tr>
		<td width="140">
			Rotating Right (Portrait)
		</td>
		<td width="185">
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
			python3 driver.py -d 1
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
			python3 driver.py -d 1
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
			GIF: after each rotation, the display is calibrated to where the movement of the cursor is accurate and consistent.
		</td>
		<td>
			<img src="./.github_readme/gif/tracking.gif" width="256"/>
		</td>
	</tr>
</table>