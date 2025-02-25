"""
Дан лог поиска
в нем группы строк разделенные пустой строкой
первая строка в группе - это путь
остальные строки - это строки с информацией
нужно найти все группы, в которых есть фрагмент: '"owner": "andrey.valentynovich@karuna.group"'
и записать их в файл информацию из них в формате:
путь, andrey.valentynovich@karuna.group


лог поиска:
---
dags/marketing/bots/acqusition_pa_bot/dag.py:
  28      roles=["Marketing"],
  29:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2024, 11, 17)},
  30      max_active_runs=1,

...

dags/product/report/funnel_affiliate_product/dags.py:
  35      doc_md=__doc__,
  36:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2024, 11, 1)},
  37      schedule=AFFILIATE_PRODUCT_FUNNEL_SCHEDULE,
---

"""

from pprint import pprint


LOG = """

dags/marketing/bots/acqusition_pa_bot/dag.py:
  28      roles=["Marketing"],
  29:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2024, 11, 17)},
  30      max_active_runs=1,

dags/marketing/bots/appsflyer_validation_bot/dag.py:
  28      roles=["Bi"],
  29:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 3, 25)},
  30      max_active_runs=1,

dags/marketing/bots/others_traffic_bot/dag.py:
  30      roles=["Bi"],
  31:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 3, 1)},
  32      max_active_runs=1,

dags/marketing/business/fraud_users_list/fraud_users_list.py:
  68      dag_id=FRAUD_USERS_LIST_DAG_ID,
  69:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 1, 1)},
  70      schedule=FRAUD_USERS_LIST_SCHEDULE,

dags/marketing/business/invest_fact/adwords/dag.py:
  25      default_args={
  26:         "owner": "andrey.valentynovich@karuna.group",
  27          "start_date": pendulum.datetime(2023, 5, 30),

dags/marketing/business/invest_fact/dbm/dag.py:
  22      dag_id=DBM_INVEST_DAG_ID,
  23:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2022, 6, 30)},
  24      schedule=DBM_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/dv360/dag.py:
  27      dag_id=DV360_INVEST_DAG_ID,
  28:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2022, 5, 1)},
  29      schedule=DV360_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/facebook/dag.py:
  21      fl=__file__,
  22:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  23      schedule=FACEBOOK_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/influencer/dag.py:
  21      dag_id=INFLUENCER_INVEST_DAG_ID,
  22:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2020, 10, 1)},
  23      schedule=INFLUENCER_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/invest_erp/dag.py:
  35      dag_id=INVEST_ERP_DAG_ID,
  36:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2020, 10, 1)},
  37      schedule=INVEST_ERP_SCHEDULE,

dags/marketing/business/invest_fact/invest_marketing/dag.py:
  72      dag_id=INVEST_MARKETING_DAG_ID,
  73:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2020, 10, 1)},
  74      schedule=INVEST_MARKETING_SCHEDULE,

dags/marketing/business/invest_fact/marketing_partner_metrics/dag.py:
  42      dag_id=MARKETING_PARTNER_METRICS_DAG_ID,
  43:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2020, 10, 1)},
  44      schedule=MARKETING_PARTNER_METRICS_SCHEDULE,

dags/marketing/business/invest_fact/networks/dag.py:
  23      fl=__file__,
  24:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  25      dag_id=NETWORKS_DAG_ID,

dags/marketing/business/invest_fact/networks_invest_from_af/dag.py:
  36      dag_id=NETWORKS_INVEST_FROM_AF_DAG_ID,
  37:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  38      schedule=NETWORKS_INVEST_FROM_AF_SCHEDULE,

dags/marketing/business/invest_fact/pa_invest/dag.py:
  85      dag_id=PA_INVEST_DAG_ID,
  86:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2020, 10, 1)},
  87      schedule=PA_METRICS_SCHEDULE,

dags/marketing/business/invest_fact/paid_search_manual_invest/dag.py:
  41      fl=__file__,
  42:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 31)},
  43      schedule=PAID_SEARCH_MANUAL_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/revshare/dag.py:
  21      dag_id=REVSHARE_INVEST_DAG_ID,
  22:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  23      schedule=REVSHARE_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/unity/dag.py:
  25      fl=__file__,
  26:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  27      schedule=UNITY_INVEST_SCHEDULE,

dags/marketing/business/invest_fact/yandex/dag.py:
  26      fl=__file__,
  27:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  28      schedule=YANDEX_INVEST_SCHEDULE,

dags/marketing/business/orders_interaction_last/dag.py:
  68      default_args={
  69:         "owner": "andrey.valentynovich@karuna.group",
  70          "start_date": pendulum.datetime(2022, 10, 31),

dags/marketing/business/runrates/dag.py:
  45      default_args={
  46:         "owner": "andrey.valentynovich@karuna.group",
  47          "start_date": pendulum.datetime(2025, 1, 28),  # original start date = (2022, 6, 1)

dags/marketing/business/runrates/facts_for_rr/dag.py:
  88      default_args={
  89:         "owner": "andrey.valentynovich@karuna.group",
  90          "start_date": pendulum.datetime(2024, 10, 1, 0, 0, 0),

dags/marketing/business/runrates/facts_for_rr_test/dag.py:
  63      fl=__file__,
  64:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": START_DATE, "retries": 10},
  65      schedule=FACTS_FOR_RR_SCHEDULE,

dags/marketing/business/runrates/runrates_invest/dag.py:
  57      default_args={
  58:         "owner": "andrey.valentynovich@karuna.group",
  59          "start_date": pendulum.datetime(2025, 1, 28),  # original start date = (2023, 1, 1)

dags/marketing/business/runrates_reference/dag.py:
  41      default_args={
  42:         "owner": "andrey.valentynovich@karuna.group",
  43          "start_date": pendulum.datetime(2025, 1, 28),  # original start date = (2022, 1, 1)

dags/marketing/business/touchpoint/upload_appsflyer_id_customer_id.py:
  24      default_args={
  25:         "owner": "andrey.valentynovich@karuna.group",
  26          "start_date": pendulum.datetime(2022, 5, 1),

dags/marketing/business/touchpoint/upload_touchpoint_crm.py:
  23      default_args={
  24:         "owner": "andrey.valentynovich@karuna.group",
  25          "start_date": pendulum.datetime(2022, 1, 1),

dags/marketing/business/touchpoint/upload_touchpoint_mob.py:
  30      default_args={
  31:         "owner": "andrey.valentynovich@karuna.group",
  32          "start_date": pendulum.datetime(2021, 1, 1),

dags/marketing/business/user_sa_status/dag.py:
  24      default_args={
  25:         "owner": "andrey.valentynovich@karuna.group",
  26          "start_date": pendulum.datetime(2014, 11, 17),

dags/marketing/exports/adc_payouts/dag.py:
  32      dag_id=ADC_PAYOUTS_GOOGLE_SHEETS_DAG_ID,
  33:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2024, 2, 21)},
  34      schedule=ADC_PAYOUTS_GS_SCHEDULE,

dags/marketing/exports/appfollow/update_ranking.py:
  25      fl=__file__,
  26:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2022, 9, 1)},
  27      schedule=APPFOLLOW_RANKING_SCHEDULE,

dags/marketing/raw/adcombo_tableau_full_reference/update.py:
  33      schedule=PA_REFERENCE_BY_CAMPAIGNS_SCHEDULE,
  34:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 1, 1)},
  35      roles=["Bi"],

dags/marketing/raw/currency_load/update.py:
  21      dag_id=RAW_CURRENCY_LOAD_DAG_ID,
  22:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": START_DATE},
  23      schedule=CUR_SCHEDULE,

dags/marketing/raw/invest_marketing/dv360/dag.py:
  26      fl=__file__,
  27:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2022, 5, 1)},
  28      dag_id=DV360_RAW_DAG_ID,

dags/marketing/raw/invest_marketing/facebook/dag.py:
  27      fl=__file__,
  28:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  29      schedule=FACEBOOK_INVEST_SCHEDULE,

dags/marketing/raw/invest_marketing/networks/dag.py:
  33      fl=__file__,
  34:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  35      schedule=NETWORKS_INVEST_SCHEDULE,

dags/marketing/raw/invest_marketing/unity/dag.py:
  26      fl=__file__,
  27:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 5, 30)},
  28      schedule=UNITY_INVEST_SCHEDULE,

dags/marketing/raw/isdayoff/dag.py:
  26      dag_id=MARKETING_RAW_ISDAYOFF_DAG_ID,
  27:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 1, 1)},
  28      schedule=MARKETING_RAW_ISDAYOFF_SCHEDULE,

dags/marketing/raw/pa_reference_by_campaigns/update.py:
  32      schedule=PA_REFERENCE_BY_CAMPAIGNS_SCHEDULE,
  33:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2023, 1, 1)},
  34      roles=["Bi"],

dags/product/business/ab_test_vip_sales_split.py:
  176      doc_md=__doc__,
  177:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": START_DATE},
  178      schedule="20 2 * * 2",  # Вторник 2:20

dags/product/report/feature_availability_by_date.py:
  6  START_DATE = 2022-07-25
  7: Author: andrey.valentynovich@karuna.group, created at: 2022-07-25

dags/product/report/feature_availability/dag.py:
  27      doc_md=__doc__,
  28:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": START_DATE},
  29      schedule="@daily",

dags/product/report/funnel_affiliate_product/dags.py:
  35      doc_md=__doc__,
  36:     default_args={"owner": "andrey.valentynovich@karuna.group", "start_date": pendulum.datetime(2024, 11, 1)},
  37      schedule=AFFILIATE_PRODUCT_FUNNEL_SCHEDULE,
  
"""


def find_owner(log_str: str) -> list[dict[str, str]]:
    """
    Функция поиска владельца
    :param log: лог
    :return: список списков строк с владельцем
    """
    result = []
    for group in log_str.split("\n\n"):
        if '"owner": "' in group:
            path = (group.split("\n")[0].strip(":")).strip()
            owner = group.split('"owner": "')[1].split('"')[0]
            result.append(dict({"path": path, "owner": owner}))
    return result


def write_to_file(data: list[dict[str, str]], file_name: str):
    """
    Функция записи в файл
    :param data: данные
    :param file_name: имя файла
    """
    with open(file_name, "w", encoding="utf-8") as file:
        for line in data:
            file.write(f"{line['path']}, {line['owner']}\n")


if __name__ == "__main__":

    owners = find_owner(LOG)
    write_to_file(owners, "owners.txt")
    pprint(owners)
