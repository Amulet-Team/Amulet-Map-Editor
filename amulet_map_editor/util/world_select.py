class WorldUI:
    # UI element that holds the world image, name and description
    pass


class WorldUIButton:
    # a button that wraps around WorldUI so that WorldUI can be used without the button functionality
    pass


class WorldDirectoryUI:
    # a drop down list of `WorldUIButton`s for a given directory
    pass


class WorldSelectUI:
    # a frame containing a refresh button for the UI, a sort order for the worlds
    # and a vertical list of `WorldDirectoryUI`s for each directory
    # perhaps also a select directory option
    pass