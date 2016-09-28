#!/usr/bin/env python

import argparse
from core.projects.LangProject import LangProject
from core.projects.MathProject import MathProject
from core.projects.ChartProject import ChartProject
from core.projects.TimeProject import TimeProject
from core.projects.ClosureProject import ClosureProject

from core.Config import conf

from core.tools.NopolPC import NopolPC
from core.tools.NopolC import NopolC
from core.tools.BrutpolPC import BrutpolPC
from core.tools.BrutpolC import BrutpolC

heapsize="-Xmx1024m"

def initParser():
    parser = argparse.ArgumentParser(description='Runner for ci NoPol')
    parser.add_argument('-project', required=True, help='Which project (all, math, lang, time)')
    parser.add_argument('-tool', required=True, help='Which tool (nopol,  ...)')
    parser.add_argument('-id',  help='Bug id')
    parser.add_argument('-heap', help='specified the size of the java heap (-Xmx1024m, -Xmx2048m, -Xmx4096m')
    return parser.parse_args()

args = initParser()
project = None
tool = None
id = int(args.id)

if args.heap is not None:
    conf.setHeapSize("-" + args.heap)

if args.project == "Lang":
    project = LangProject()
elif args.project == "Math":
    project = MathProject()
elif args.project == "Chart":
    project = ChartProject()
elif args.project == "Time":
    project = TimeProject()
elif args.project == "Closure":
    project = ClosureProject()

if args.tool == "NopolPC":
    tool = NopolPC()
elif args.tool == "NopolC":
    tool = NopolC()
elif args.tool == "BrutpolPC":
    tool = BrutpolPC()
elif args.tool == "BrutpolC":
    tool = BrutpolC()

tool.run(project, id)
