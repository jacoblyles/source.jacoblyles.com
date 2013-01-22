import os
import argparse
import subprocess

import staticjinja

outdir = "./out"

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='build jacoblyles.com')
  parser.add_argument('--deploy',
                   help='deployment directory for static files. (default: none)')

  args = parser.parse_args()
  if (args.deploy):
    staticjinja.main(autoreload=False, outpath='./out')
    argstring = 'cp -r %s %s' %(os.path.join(outdir,'*'), args.deploy)
    print argstring
    print os.getcwd(), __file__
    subprocess.call(argstring, shell=True)
  else:
    staticjinja.main(outpath='./out')