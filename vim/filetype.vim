if exists("did_load_filetypes")
  finish
endif
augroup filetypedetect
    au BufRead,BufNewFile *.q setfiletype q
  " au! commands to set the filetype go here
augroup END
