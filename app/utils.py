
def get_metadata_args(metadata):
    """
    Add metadata arguments to a list for postprocessing.
    """

    metadata_args = []
    for metadata_type in ('title', 'artist', 'genre', 'album'):
        if metadata[metadata_type]:
            metadata_args += ['-metadata', f'{metadata_type}={metadata[metadata_type]}']

    return metadata_args

def get_trim_video_args(start, end):
    """
    Add trimming times to a list for postprocessing.
    """

    trim_args = []
    if start and end:
        trim_args = ['-ss', start, '-to', end]
    elif start:
        trim_args = ['-ss', start]
    elif end:
        trim_args = ['-ss', '00:00:00', '-to', end]

    return trim_args
    