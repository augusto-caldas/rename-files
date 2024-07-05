# rename-files
Script                    | How it works<br>
remove_brackets           | Remove all brackets and the content inside of it. Example: "movie (1080p).mkv" -> "movie.mkv".<br>
rename_files_10           | Rename files to S<season>E0<counter>. Example: S01E01...S01E99.<br>
rename_files_100          | Rename files to S<season>E00<counter>. Example: S01E001...S01E999.<br>
rename_directory          | Rename directory based on file name excluding extension. Example: "movie/movie-a.mkv" -> "movie-a/movie-a.mkv"<br>
order_episode_from_file  | Reads a file with structure S00E00, And goes over the episodes with just name compare it to file and add the matching episode number. Example: "episode name.mkv" -> "S01E01 - episode name.mkv"
