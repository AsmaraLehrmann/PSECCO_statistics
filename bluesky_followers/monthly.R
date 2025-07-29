# bluesky_followers/monthly.R
# Install bskyr if not already installed
if (!requireNamespace("bskyr", quietly = TRUE)) {
  install.packages("bskyr", repos = c("https://christopherkenny.r-universe.dev", "https://cloud.r-project.org"))
}

library(bskyr)

handle <- "polarsecco.bsky.social"
profile <- bs_get_profile(handle)

if (!is.null(profile)) {
  count <- profile$followersCount
  today <- Sys.Date()

  df <- data.frame(date = today, handle = handle, followers = count)

  dir.create("bluesky_followers/data", recursive = TRUE, showWarnings = FALSE)
  write.table(
    df,
    "bluesky_followers/data/bsky_followers.csv",
    sep = ",",
    row.names = FALSE,
    col.names = !file.exists("bluesky_followers/data/bsky_followers.csv"),
    append = TRUE
  )

  cat(today, ": ", handle, " has ", count, " followers\n")
} else {
  stop("Failed to retrieve Bluesky profile.")
}
