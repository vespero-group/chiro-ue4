import lzma
import json
import os.path


def _chrom1xz_loader(source):
    source_path = os.path.join(
        os.path.dirname(__file__),
        'data',
        source
    )

    with lzma.open(source_path, mode='r') as fd:
        data = json.load(fd)

    return data


SCHEMA = {
    'id': 'mannequin',
    'name': 'Mannequin',
    'variants': [
        {
            'id': 'pose-a',
            'name': 'A-Pose',
            'load_data': lambda: _chrom1xz_loader('pose_a.chrom1xz')
        },
        {
            'id': 'pose-t',
            'name': 'T-Pose',
            'load_data': lambda: _chrom1xz_loader('pose_t.chrom1xz')
        }
    ]
}
