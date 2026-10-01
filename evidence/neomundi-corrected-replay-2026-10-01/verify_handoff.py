#!/usr/bin/env python3
"""Verify this evidence handoff, then replay unchanged code in a temporary copy."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile
ROOT = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    manifest = json.loads((ROOT / 'HANDOFF_MANIFEST.json').read_text())
    expected = {x['path'] for x in manifest['files']}
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name not in ['HANDOFF_MANIFEST.json', 'HANDOFF_MANIFEST.sha256']}
    assert expected == actual, 'File inventory changed'
    for e in manifest['files']:
        p = ROOT / e['path']
        assert sha(p) == e['sha256'] and p.stat().st_size == e['bytes'], e['path']
    assert (ROOT / 'HANDOFF_MANIFEST.sha256').read_text().split()[0] == sha(ROOT / 'HANDOFF_MANIFEST.json'), 'Manifest checksum'
    c = ROOT / 'corrected_evidence'
    original = ROOT / 'historical/original_payloads'
    results = json.loads((c / 'evidence/NEOMUNDI_OGS_PRIVATE_PILOT_RESULTS_v0_1_1_CORRECTED.json').read_text())['results']
    receipts = json.loads((c / 'evidence/NEOMUNDI_OGS_CAOM_LITE_RECEIPT_BUNDLE_v0_1_1_CORRECTED.json').read_text())['receipts']
    names = sorted(p.name for p in (c / 'payloads').glob('*.json'))
    assert len(names) == len(results) == len(receipts) == 5, 'Must contain all five preserved cases'
    assert sorted(x['file'] for x in results) == sorted(x['source_file'] for x in receipts) == names, 'Case identities'
    for name in names:
        assert (original / name).read_bytes() == (c / 'payloads' / name).read_bytes(), name
        r = next(x for x in results if x['file'] == name)
        receipt = next(x for x in receipts if x['source_file'] == name)
        assert sha(c / 'payloads' / name) == r['input_hash'] == receipt['input_hash'], name
    with tempfile.TemporaryDirectory(prefix='neomundi-replay-') as d:
        tmp = Path(d) / 'corrected'
        shutil.copytree(c, tmp)
        process = subprocess.run([sys.executable, str(tmp / 'verification/verify_and_replay.py')], capture_output=True, text=True)
        if process.returncode:
            raise RuntimeError(process.stdout + process.stderr)
        replay = json.loads((tmp / 'evidence/NEOMUNDI_OGS_REPLAY_EXECUTION_RESULT_v0_1_1.json').read_text())
        assert replay['passed'] == 5 and replay['failed'] == 0 and len(replay['cases']) == 5, 'Replay did not cover five cases'
        assert replay == json.loads((ROOT / 'fresh_verification/corrected_replay_result.json').read_text()), 'Replay differs from recorded result'
    print('PASS: handoff manifest, five original/corrected payloads and receipt bindings; unchanged corrected replay: 5 passed, 0 failed.')
    print('Scope: synthetic package replayability and consistency. Not independent external validation or live integration.')
if __name__ == '__main__':
    try: main()
    except Exception as exc:
        print('FAIL:', str(exc), file=sys.stderr)
        sys.exit(1)
