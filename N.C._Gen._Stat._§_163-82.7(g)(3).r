library(readr)
library(dplyr)
library(tidyr)
library(data.table)

df <- read_csv("/Users/klausmayr/Desktop/VR/2022_Election/denied/absentee_20221108.csv")

# Load in the voter registration data
vr <- fread("/Users/klausmayr/Downloads/converted_VR_Snapshot_20230101.txt",
            select = c("voter_status_desc", "precinct_abbrv", "zip_code", "voter_reg_num", "ncid", "last_name","county_desc","race_code","age", "voter_status_reason_desc", "cancellation_dt"))

vr_denied <- vr %>%
  subset(voter_status_desc == "DENIED") %>%
  mutate(denied_date = as.Date(cancellation_dt)) %>%
  filter(denied_date > "2022-01-01")

df_recent <- df %>%
  mutate(voter_reg_num = as.numeric(voter_reg_num)) %>%
  mutate(voted_date = as.Date(ballot_rtn_dt, format = "%m/%d/%Y")) %>%
  filter(voted_date > "2022-01-01")

new_df <- inner_join(df_recent, vr_denied, by = c("voter_reg_num" = "voter_reg_num", "voter_last_name" = "last_name"))
dates_df <- subset(new_df, select = c("county_desc.x","voter_reg_num", "ncid.x", "voted_date","denied_date","voter_status_desc",
                                      "voter_first_name","voter_last_name","voter_first_name", "voter_middle_name", "race", "ethnicity"
                                      ,"gender","age.x","voter_city","voter_zip","voter_party_code","precinct_desc",
                                      "denied_date", "mail_veri_status","ballot_rtn_status", "ballot_req_type", "ballot_req_delivery_type",
                                      "ballot_req_type", "ballot_req_dt", "ballot_send_dt", "ballot_rtn_dt", "ballot_rtn_status",
                                      "site_name", "sdr"
                                      ))

voted_after_denied <- dates_df[dates_df$denied_date > dates_df$voted_date,]
