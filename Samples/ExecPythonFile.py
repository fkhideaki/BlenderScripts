import bpy
import os

def executePython(dir, fname):
    fn = os.path.join(dir, fname)
    with open(fn) as f:
        fb = f.read()
        py = compile(fb, fname, 'exec')
        exec(py)
