# Edit Program

## About

The edit program is a 3D world editor with similarities to MCEdit Unified. The user can select an area and run various operations on that area.

![edit](../../../resource/img/edit.jpg)

## Controls

The controls are currently hard coded but in the future they will be customisable. They are as follows:
- forward: W
- backward: S
- left: A
- right D
- down: Shift
- up: Spacebar
- toggle camera rotation: middle click or double right click
- select box corner: Left click
- change mouse select mode: Right click (options are closest non-air block and fixed distance)
- change fly speed: Middle mouse scroll

## Tools

On the left should be a bar of buttons which control different things in the editor.

Dimension: Select which dimension is active
Undo: Undo the last change. (ctrl+z)
Redo: Reapply an undone change. (ctrl+y)
Save: Save all changes to the world. Any changes in the editor are saved in the editor until the user requests them to be saved to the world. (ctrl+s)
Close: Close the current world.

### Operations

The section below this is the operation section.

There is a drop down list of operations that come with Amulet and user created operations.

Below that is a button to change the options for the selected operation. This may be grayed out of the plugin does not require options.

Below that is a button that will run the operation. Some operations may require a selection of the world to run on and the user will be notified if this is the case but not all operations do.

### Fill and Replace
- Select an area of the world you would like the operation to run on.
- Select the operation from the list of operations.
- Fill: Select the block you wish to fill the area with.
- Replace: Select the block you would like to replace (use * to match any value of that property) and select the block you would like to fill it with.
-Run the operation.
-Undo will undo the changes and save will apply them to the world files.


### Delete Chunks
- Like with fill and replace select an area and select the operation. This operation will delete all chunks the selection overlaps with even if only partially selected.
- Run the operation and the chunks will be deleted.
- Undo will undo the changes and save will apply them to the world files.

### Clone
- Select an area, select the operation and click run operation.
- The operation screen will change to allow you to pick a destination location.
- Type in the coordinate where you want it to be placed or use middle mouse wheel while hovering on a number.
- Click "Confirm" to paste the selection at the new location or "Cancel" to cancel

### Copy and Paste
- Select an area and press ctrl+c to copy (or Edit -> Copy)
- Press ctrl+v (or Edit -> Paste) to choose where to paste the selection in the world. See [clone](#clone) for more information
- It is worth noting here that Amulet is able to have multiple worlds open at the same time and the copied area can be pasted into a different world.
- Our translation system also handles conversion between different world formats so the source and destination worlds do not need to be from the same version or platform.
