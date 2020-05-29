# import modules
import csv
import numpy as np
import pandas as pd
from statistics import mean

def post_feedback(org, role, view, activity, context, feedback, decision):
  '''
  This function gets the above fields,
  add them as the last row in the extended pap,
  if there is enough new probabilities, it updates the pap
  '''
  pap_path = 'csv_pap.csv'
  xap_path = 'csv_xap.csv'
  pap = pd.read_csv(pap_path)
  xap = pd.read_csv(xap_path)

  # get the fields
  fields = [org, role, view, activity, context, feedback, decision]

  # add the fields as the last row in the extended pap
  with open(xap_path, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

  # check if we have reached the treshold
  treshold = 1
  statement1 = (xap['org'] == org) & (xap['role'] == role) & (xap['view'] == view) & (xap['activity'] == activity) & (xap['context'] == context)
  xdf = xap.loc[statement1]
  if (xdf.shape[0] <= treshold):
    updated_proba = feedback
  else :
    updated_proba = mean(list(xdf['proba']))

    # update proba in PAP (df contains just one row, no duplicates in PAP)
    statement2 = (pap['org'] == org) & (pap['role'] == role) & (pap['view'] == view) & (pap['activity'] == activity) & (pap['context'] == context)
    pap.loc[statement2, 'proba'] = round(updated_proba, 2)
    # save pap
    # save empower S-R
    new_pap = pap.to_csv('pap_updated.csv', index = False)

  return [org, role, view, activity, context, round(updated_proba, 2), decision]

#'BV BXZ','m QIX','XYC','TF48','JYQF',0.11
post_feedback('BV BXZ','m QIX','XYC','TF48','JYQF',0.19, 'permitted')
