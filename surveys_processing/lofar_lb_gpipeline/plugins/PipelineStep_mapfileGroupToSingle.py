import os
from lofarpipe.support.data_map import DataMap
from lofarpipe.support.data_map import DataProduct


# Colm Coughlan, March 2016
# used in locapi generic pipeline implementation


def plugin_main(args, **kwargs):
    """
    Takes in mapfile_in, containing many files, and returns only one

    Parameters
    ----------
    mapfile_in : str
        Name of the input mapfile to be trimmed back.
    mapfile_dir : str
        Directory for output mapfile
    filename: str
        Name of output mapfile

    Returns
    -------
    result : dict
        Output datamap filename

    """
    mapfile_dir = kwargs['mapfile_dir']
    filename = kwargs['filename']

    inmap = DataMap.load(kwargs['mapfile_in'])
    if len(inmap)<1:
		print('ERROR: GroupToSingle: mapfile_in has size < 1.')
		return(1)


    map_out = DataMap([])
    map_out.data.append(DataProduct(inmap[0].host, inmap[0].file, inmap[0].skip ))

    fileid = os.path.join(mapfile_dir, filename)
    map_out.save(fileid)
    result = {'mapfile': fileid}

    return result
