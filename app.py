"""Flask application for the web interface."""
# coding=utf-8
import sys
import os

# Flask utils
from flask import Flask, request, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './scripts')))
#