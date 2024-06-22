import csv
import io
from datetime import datetime

import pandas as pd
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from produto.models.produto_model import Produto


