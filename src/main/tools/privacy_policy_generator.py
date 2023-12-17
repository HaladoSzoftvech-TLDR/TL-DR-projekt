import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from main.tools.pp_samples import *
import csv
import random

components = ["My", "Your", "Special", "Awesome", "Super", "Web", "Tech", "Data", "Cloud", "Digital", "Smart", "Quick",
              "Express", "Global", "Future", "Dynamic", "Innovative", "Agile", "Creative", "Unique", "Enterprise",
              "Power", "Info", "Eco", "Green", "Prime", "Ultra", "Mega", "Pro"]

service_names = [random.choice(components) + random.choice(components) + random.choice(components) for _ in range(100)]

data_types = ["Name", "Email Address", "Order History", "Postal address", "Phone number",
              "Birth date", "Ip address", "Age", "Gender", "Marital status", "Fingerprint",
              "Job title", "Company name", "Medical history", "Username", "Bank account information"]
retention_period_type = ["years", "month"]
user_rights = ["Access to your data", "Deletion of data", "Rectification of data",
               "Erasure of data", "Right to Restriction of Processing", "Data Portability", "To Object",
               "Rights Related to Automated Decision Making, Including Profiling", "Right to Withdraw Consent",
               "Information"]

samples = [sample_1, sample_2, sample_3, sample_4, sample_5, sample_6, sample_7, sample_8, sample_9, sample_10,
           sample_11]


def generate_privacy_policy(template_string, service_name, data_types, retention_period, user_rights):
    privacy_policy = Template(template_string).render(
        service_name=service_name,
        data_types=data_types,
        retention_period=retention_period,
        user_rights=user_rights
    )

    return privacy_policy


def generate_pp():
    sn = random.sample(service_names, 1)
    data_num = random.randrange(len(data_types) - 1) + 1
    dts = random.sample(data_types, data_num)
    rpt = random.sample(retention_period_type, 1)
    ur_num = random.randrange(len(user_rights) - 1) + 1
    urs = random.sample(user_rights, ur_num)
    smp = random.sample(samples, 1)
    ret_p = str(random.randrange(29) + 1) + " " + rpt[0]
    pp = generate_privacy_policy(smp[0], sn[0], dts,
                                 ret_p, urs)
    res_str = ("The name of the company is " + sn[0] + ". The data types they collect are " +
               ", ".join(dts) + ". The retention period is " + ret_p +
               ". The user rights are " + ", ".join(urs) + ".")
    return [res_str, pp]


def generate_pp_for_test():
    sn = random.sample(service_names, 1)
    data_num = random.randrange(len(data_types) - 1) + 1
    dts = random.sample(data_types, data_num)
    rpt = random.sample(retention_period_type, 1)
    ur_num = random.randrange(len(user_rights) - 1) + 1
    urs = random.sample(user_rights, ur_num)
    smp = random.sample(samples, 1)
    ret_p = str(random.randrange(29) + 1) + " " + rpt[0]
    pp = generate_privacy_policy(smp[0], sn[0], dts,
                                 ret_p, urs)
    res_str = {"company_name": sn[0], "collected_data_types": dts, "retention_period": ret_p, "user_right": urs}
    return [res_str, pp]


def write_csv(number_of_pps: int):
    with open('./data/summary.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["text", "ctext"])
        for i in range(number_of_pps):
            writer.writerow(generate_pp())
