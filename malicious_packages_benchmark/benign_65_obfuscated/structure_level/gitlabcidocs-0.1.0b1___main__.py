import pathlib
if False:
    _var_42_0 = (313, 9, 102)
    _var_42_1 = (568, 750, 313)
    _var_42_2 = (566, 727, 860)

    def _var_42_fn():
        pass
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import docsgen
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--include-all-rules', required=False, default=True, action='store_true', help='If true, document all workflow rules. Otherwise only rules with $CI_PIPELINE_SOURCE=web|pipeline|api are included')
    parser.add_argument('--ci-file', required=False, default='.gitlab-ci.yml', help='Path to gitlab-ci.yml')
    parser.add_argument('--doc-file', required=False, default='README.md', help='Path to the file in the docs are injected to')
    if False:
        _var_41_0 = (747, 504, 720)
        _var_41_1 = (985, 527, 173)

        def _var_41_fn():
            pass
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_arguments()
    docsgen.create_docs(args.ci_file, args.doc_file, args.include_all_rules)
if False:
    _var_43_0 = (303, 677, 665)

    def _var_43_fn():
        pass