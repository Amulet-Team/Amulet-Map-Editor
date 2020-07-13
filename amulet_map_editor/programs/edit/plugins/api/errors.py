class BaseOperationException(Exception):
    pass


class OperationError(BaseOperationException):
    """Error to raise if something went wrong when running the operation.
    Will notify the user with a dialog box with the message f"Error running operation {msg}"
    Changes will be rolled back to the last backup.
    Eg. if the operation requires something it is not given"""

    pass


class OperationSuccessful(BaseOperationException):
    """raise this if you want to exit the operation without creating an undo point.
    Will notify the user with a dialog box containing the message.
    Changes will be rolled back to the last backup."""

    pass


class OperationSilentAbort(BaseOperationException):
    """Error to raise if something went wrong when running the operation but you do not want the user to see.
    This error will be handled silently.
    Changes will be rolled back to the last backup."""

    pass
