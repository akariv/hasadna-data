# *** encoding: utf-8 ***

import os
import json
import time

source = "משרד האוצר"
notes = "סעיף זה נגזר בצורה אוטומטית מנתוני משרד האוצר"

input_fn = os.path.join('..','..','gov','mof','budget','budget.jsons')

out = {}
titles = {}
for line in file(input_fn):
    rec = json.loads(line)
    code = rec['code']
    year = rec['year']
    title = rec.get('title')
    if title == None:
        title = titles.get((code,year))
    if title == None:
        continue 
    key=(title,code)
    out.setdefault(key,{}).setdefault(year,{}).update(rec)
    titles[(code,year)] = title

refs = {}
for line in file(input_fn):
    rec = json.loads(line)
    code = rec['code']
    year = rec['year']
    slug = rec['slug']
    if code == '00' or code == '0000':
        continue
    
    parent_code = code
    while True:
        parent_code = parent_code[:-2]
        if parent_code == '':
            break
        parent_title = titles.get((parent_code,year))
        if parent_title == None:
            continue
        parent_key=(parent_title,parent_code)
        refs.setdefault(parent_key,{})[(year,code)] = slug
        break

ok = out.keys()
ok.sort(key=lambda x:x[1])    
for k in ok:
    v = out[k]
    title,code = k
    
    sums = {}
    for year,rec in v.iteritems():
        sums[year] = dict([(k1,v1) for k1,v1 in rec.iteritems() if ('net' in k1 or 'gross' in k1)])
    
    _refs = refs.get(k,{}).values()
    
    rec =  { "slug"     : "%s_%s" % ( code, title.encode('iso8859-8').encode('hex') ),
             "title"    : title,
             "notes"    : notes,
             "source"   : source,
             "timestamp": time.ctime(),
             "sums"     : sums,
             "refs"     : _refs,
            "parts"     : [1.0] * len(_refs) 
            }
    print json.dumps(rec) 
