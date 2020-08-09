import bpy
import os


def _gen_save_filepaths(extension):
    blend_filepath = bpy.data.filepath
    blend_file = os.path.basename(blend_filepath)
    folder = os.path.abspath(os.path.dirname(blend_filepath))
    fname, _ = os.path.splitext(blend_file)

    clean_name = os.path.join(folder, "{}.{}".format(fname, extension))

    idx = 0
    while True:
        idx += 1
        next_suffix = os.path.join(
            folder, "{}-v{:02}.{}".format(fname, idx, extension))
        if os.path.exists(next_suffix):
            continue
        break

    last_suffix = os.path.join(
        folder,
        "{}-v{:02}.{}".format(fname, idx-1, extension)
    )

    return clean_name, next_suffix, last_suffix


def get_gen_options_callback(extension):
    def gen_options(self, ctx):
        clean_name, next_suffix, last_suffix = _gen_save_filepaths(extension)
        options = []

        clean_filename = os.path.basename(clean_name)
        next_filename = os.path.basename(next_suffix)
        last_filename = os.path.basename(last_suffix)

        if not os.path.exists(clean_name):
            options.append((clean_name, 'Save as "{}"'.format(
                clean_filename), 'Save to {}'.format(clean_name)))
        else:
            options.append((clean_name, 'Replace "{}"'.format(
                clean_filename), 'Save to {}'.format(clean_name)))

        if not os.path.exists(last_suffix):
            options.append((last_suffix, 'Save as "{}"'.format(
                last_filename), 'Save to {}'.format(last_suffix)))
        else:
            options.append((next_suffix, 'Save as "{}"'.format(
                next_filename), 'Save to {}'.format(next_suffix)))
            options.append((last_suffix, 'Replace "{}"'.format(
                last_filename), 'Save to {}'.format(last_suffix)))

        return options

    return gen_options
