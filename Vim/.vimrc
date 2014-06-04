" This vimrc file mostly just enables lots of good vim features like syntax
" hilighting, the mouse, and so forth.  However, it also defines a few hotkeys
" and commands which are listed below for reference (a few of them aren't
" actually defined here but are from plugins in the .vim folder):
"
"   F4 - Show the syntax group under the cursor.
"   F5 - Open/Close directory browser
"   F8 - Run make (Note that by default it builds with 6 cores via -j6)
"   F9 - Open/Close a window that shows changes in the file with respect
"        to what is in source control like svn,mercurial,etc.
"
"        See :help vimdiff for documentation about the diff window.  But the
"        main commands are do (for diff obtain) and dp (for diff put).  These
"        dommands let you transfer blocks of text from one window to the
"        other (the left side is your current file while the right side is
"        what is in source control)
"
"   F10 and F11 - Both of these bring up the :cwindow which shows compiler
"        errors.
"
"   F12 - Open/Close the project pane on the left.  See :help project for
"         details on how to use this plugin.
"
"   CTRL+h, CTRL+j, CTRL+k, or CTRL+l - Move the cursor from one vim split
"         screen to another.  
"
"   :A  - This command will try and jump you between a header file and its
"         corresponding source file.
"       
"   \be - This brings up the buffer explorer.  q closes the explorer or you
"         can use it to view a file you recently opened.
"   ,v  - open your vimrc file
"   ,V  - Reload your vimrc file
"   \d  - Paste the following comment into your source file:
"         // ----------------------------------------------------------------------------------
"   \c  - When in a java source file this will paste the following:
"         System.out.println(
"   \t  - Open a new tab.  This is the same as :tabnew
"

set tags+=~/source/tags
set path+=~/source

 
" Setup color options based on the supported color modes
" of the current terminal.
if has("win32")
    "color davis
    colorscheme torte
    set guifont=Courier:h10:cANSI
else
    if &term =~ "linux"
        if has("terminfo")
            set t_Co=8
            set t_Sf=[3%p1%dm
            set t_Sb=[4%p1%dm
        else
            set t_Co=8
            set t_Sf=[3%dm
            set t_Sb=[4%dm
        endif
        ""color davis8
        colorscheme torte
    elseif &term =~ "xterm" 
        set term=xterm-color
        set t_Co=16
        "color desert
        ""color davis
        colorscheme torte
    elseif &term =~ "screen" 
        set t_Co=16
        "color desert
        ""color davis
        colorscheme torte
    endif
endif

autocmd!
set nomodeline

set fileformat=unix
set fileformats=unix,dos
set encoding=utf-8 spelllang=en
autocmd FileType c,cpp,java,python,matlab,cs,k,q set textwidth=91

"enable java auto-completion via CTRL-X CTRL-O
autocmd Filetype java setlocal omnifunc=javacomplete#Complete
autocmd FileType java setlocal completefunc=javacomplete#CompleteParamsInfo
" remap CTRL-B to CTRL-X CTRL-O 
autocmd FileType java,cpp,c,python,cs inoremap <C-B> <C-X><C-O>

" use \t to open a new tab
map \t :tabnew<CR>

set nocp " Don't use vi compatability mode.

filetype indent plugin on
"set omnifunc=syntaxcomplete#Complete

syntax on
set mouse=a
set autoindent ruler

" set the spell check color options to something sane.
hi SpellBad ctermbg=1 ctermfg=15
hi SpellCap ctermbg=11

" hilight search terms
set hlsearch

" Indentation rules
autocmd FileType html,xsd,xml,xslt,c,cpp,java,sh,matlab,python,cs set cin nu cino=t0,c4,C1,(1s,l1,W4,m1,g0 
autocmd FileType conf set cin cino=+0,#0 cinkeys-=0#
autocmd FileType conf,c,cpp,python,java,sh,lout,tex,matlab,vim,cs set sw=4 ts=4 expandtab sr
autocmd FileType html,xsd,xml,xslt set sw=3 ts=3 expandtab sr
autocmd FileType conf,html,xsd,xml,xslt,c,cpp,python,java,sh,matlab,cs set formatoptions-=ro
autocmd FileType conf,html,xsd,xml,xslt,c,cpp,python,java,sh,matlab,cs set formatoptions+=n
autocmd FileType c,cpp,python,java,sh,matlab,cs set complete=.,w,b,u,t,i
autocmd FileType c,cpp set indentexpr=GetMyCppIndent() 
autocmd FileType java set indentexpr=GetMyJavaIndent() 
autocmd FileType html,xsd,xml,xslt set indentexpr=GetMyXmlIndent() 
autocmd FileType conf,lout,tex set ai 
autocmd FileType c,cpp,java,cs set spellcapcheck=[.?]\\_[\\])'\"\t\ ]\\+
autocmd FileType c,cpp,cs set indentkeys=0{,0},:,0#,!^F,o,O,e,0>,/,0),0-,0=requires,0=ensures,0=throws,0=-\ else
autocmd FileType java set indentkeys=0{,0},:,0#,!^F,o,O,e,>,/,0),0-,0=requires,0=ensures,0=throws,0=-\ else,0=\<li\>
autocmd FileType html,xsd,xml,xslt set indentkeys=!^F,o,O,e,>

" turn on spell checking for XML type files
autocmd FileType html,xsd,xml,xslt syntax spell toplevel
autocmd FileType html,xsd,xml,xslt,text setlocal spell
autocmd Filetype help setlocal nospell

" turn on spell checking for these type files
autocmd FileType c,cpp,python,java,matlab,sh,svn,tex,cs setlocal spell
autocmd BufNewFile,BufRead *.txt setlocal spell

" Ignore CamelCase words when spell checking source code.
fun! IgnoreCamelCaseSpell()
    syn match CamelCase /\<[A-Z][a-z]\+[A-Z].\{-}\>/ contains=@NoSpell transparent
    syn cluster Spell add=CamelCase
    syn match CamelCase2 /\<[a-z]\+[A-Z]\+[a-z]\+.\{-}\>/ contains=@NoSpell transparent
    syn cluster Spell add=CamelCase2
endfun
autocmd BufRead,BufNewFile,FileType c,cpp,java,python :call IgnoreCamelCaseSpell()

" Key Mappings 

",v brings up my .vimrc
",V reloads it -- making all changes active (have to save first)
map ,v :sp ~/.vimrc<CR><C-W>

map <silent> ,V :source ~/.vimrc<CR>:filetype detect<CR>:exe ":echo 'vimrc reloaded'"<CR>

" Pass to a MATLAB, k, and q indentation files.
autocmd FileType matlab runtime! indent/matlab.vim 
autocmd FileType q runtime! indent/q.vim 
autocmd FileType k runtime! indent/k.vim 

"let c_C99 = 1
"let c_minlines = 40

"autocmd FileType python set omnifunc=pythoncomplete#Complete  Use Jedi here
" instead 
autocmd FileType c set omnifunc=ccomplete#Complete
autocmd FileType cpp set omnifunc=cppomnicomplete#Complete
autocmd FileType html,xsd,xml,xslt set omnifunc=xmlcomplete#CompleteTags

let g:proj_flags = "gimstS" 
map <silent> <F11> <ESC>:Tlist<CR>
map <F4> :echo synIDattr(synID(line("."), col("."), 1), "name")<CR>
imap <silent> <F12> <ESC><Plug>ToggleProject
imap <silent> <F10> <ESC>:cwindow<CR>
map <silent> <F10> <ESC>:cwindow<CR>
imap <silent> <F11> <ESC>:cwindow<CR>
map <silent> <F11> <ESC>:cwindow<CR>
map <silent> <F9> <ESC>:call Toggle_diff()<CR>
imap <silent> <F9> <ESC>:call Toggle_diff()<CR>
map <silent> <F5> <ESC>:NERDTreeToggle<CR>
imap <silent> <F5> <ESC>:NERDTreeToggle<CR>

autocmd FileType tex,c,cpp,lout map <silent> <F8> <ESC>:wa!<CR>:make -j4<CR>
autocmd FileType tex,c,cpp,lout imap <silent> <F8> <ESC>:wa!<CR>:make -j4<CR>
" set these back to default
autocmd FileType tex,c,cpp,lout set makeprg&
autocmd FileType tex,c,cpp,lout set efm&

" Run the current python script instead of compiling it since python doesn't
" check many errors until runtime.
autocmd FileType python set makeprg=python\ %
autocmd FileType python set efm=%E\ %#File\ \"%f\"\\,\ line\ %l%.%#,%Z%m
autocmd FileType python map <silent> <F8> <ESC>:wa!<CR>:make<CR>
autocmd FileType python imap <silent> <F8> <ESC>:wa!<CR>:make<CR>

"" My additions

autocmd FileType cs map <silent> <F8> <ESC>:wa!<CR>:!gmcs -out:tfle.exe % && ./tfle.exe<CR>
autocmd FileType cs imap <silent> <F8> <ESC>:wa!<CR>:!gmcs -out:tfle.exe % && ./tfle.exe<CR>

set lines=100 
set columns=100

"" pydiction -- python tab completion

let g:pydiction_location = '~/.vim/ftplugin/pydiction/complete-dict'
let g:pydiction_menu_height = 20

"" Add Line numbering 
set nu

"" Wrap around line ends 
set whichwrap=<,>,h,l,[,]

map <C-C> "py
"map <C-V> "pp
map <C-S> :wmap <C-space> <Esc>

" Open Taglist 
nnoremap <silent> <F7> :TlistToggle<CR>

"Remap movement keys

noremap ; l
noremap l h
noremap k j
noremap j k

imap ê <Left>
imap <A-;> <Right>
imap ì <Up>
imap ë <Down>

inoremap <C-Z> <Esc> :U
set clipboard=unnamedplus

" FIX THESE MAPPINGS 
" MAKE SEPARATE COPY PASTE COMMANDS INTERNALLY AND TO CLIPBOARD

map <C-n> "+y
map <C-m> "+p

vmap <C-c> "py
nmap <C-c> "pyiw

" Uncomment this to force ctrl-V to be a paste command
"vmap <C-v> "pp
"nmap <C-v> "pP
"imap <C-v> <Esc>"ppa

nmap <S-Up> V
nmap <S-Down> V

"set term=builtin_ansi       " Make arrow and other keys work

"if !exists("autocommands_loaded")
"    let autocommands_loaded = 1
"    autocmd BufRead,BufNewFile,FileReadPost *.py source ~/.vim/python
"endif

" Remember last line in previous file edit
"au BufReadPost * if line ("'\"") > 0|if line ("'\"") <= 
"   \line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

"" Supporting Functions 
" *********************************************************************************************
function! Toggle_diff()
    if !exists("t:inDiffMode")
       let t:inDiffMode = 0
    endif

    if t:inDiffMode == 1
        let t:inDiffMode = 0

        " set these colors back to the normal for the davis color scheme
        hi cMathOperator        guifg=#ce9100 ctermfg=Blue
        hi cLogicalOperator     guifg=#ce9100 ctermfg=Blue
        hi cBinaryOperator      guifg=#ce9100 ctermfg=Blue

        exec 'bdelete ' . t:diffModeBuffer
    else
        :VCSVimDiff
        let t:inDiffMode = 1
        let t:diffModeBuffer = bufnr("%")

        " adjust these colors so you can see them in the diffed window
        hi cMathOperator        guifg=#ce9100 ctermfg=DarkBlue
        hi cLogicalOperator     guifg=#ce9100 ctermfg=DarkBlue
        hi cBinaryOperator      guifg=#ce9100 ctermfg=DarkBlue
    endif
endfunction

" *** Misc Functions ***
" **********************************************************************************************

function! FDiffoff()
   set nodiff
   set noscrollbind
   set nowrap
   set foldmethod=manual
   set foldcolumn=0
   set scrollopt=ver,jump
endfunction

command! Diffoff call FDiffoff()

" *********************************************************************************************
" Indenting Functions
" *********************************************************************************************

" This funtion assumes that it is called only for lines that  
" are actually in a comment.   It returns the line number containing 
" the start of the comment.
function! FindCommentStart(line)
   let lnum = a:line
   while getline(lnum) !~ '/\*' && lnum > 1
       let lnum = lnum - 1
   endwhile
   return lnum
endfunction

" returns 1 if this line is part of a /* */ style comment, 0 otherwise
function! InJavaComment(line)
    let lnum = a:line
    if getline(lnum) =~ '^\s*/\*' || getline(lnum) =~ '^\s*\*/' 
       return 1
    endif

    " if this is a // style comment then return 0
    if getline(lnum) =~ '^\s*//'
       return 0
    endif

    let id = synIDattr(synID(lnum,1,0),"name")
    if synIDtrans(synID(lnum,1,0)) == hlID("Comment") || id =~ "javaCommentTitle" || id =~ "javaDocComment" || id =~ "javaDocTags" 
        return 1 
    else
        return 0 
    endif
endfunction
   
" returns 1 if this line is part of a /* */ style comment, 0 otherwise
function! InCppComment(line)
    let lnum = a:line
    if getline(lnum) =~ '^\s*/\*' || getline(lnum) =~ '^\s*\*/' 
       return 1
    endif

    " if this is a // style comment then return 0
    if getline(lnum) =~ '^\s*//'
       return 0
    endif

    if synIDtrans(synID(lnum,1,0)) == hlID("Comment") 
        return 1 
    else
        return 0 
    endif
endfunction
   
" returns the number of leading spaces on the given line
function! CountLeadingSpaces(line)
    return strlen(matchstr(getline(a:line),'^\s*'))
endfunction

function! GetMyJavaIndent()
    let theIndent = cindent(v:lnum)
    let cur = getline(v:lnum)
    let prev = getline(v:lnum-1)
    let curcount = CountLeadingSpaces(v:lnum)
    let prevcount = CountLeadingSpaces(v:lnum-1)

    " Don't format comments unless they are my formal comments.  
    " Then format them but only how I say :)
    if InJavaComment(v:lnum)
       " if this is the start of a formal comment block
       if cur =~ '^\s*/\*\*'
          return cindent(v:lnum) 
       endif

       let startnum = FindCommentStart(v:lnum)

       if startnum == v:lnum-1 && cur =~ '^\s*$'
           return CountLeadingSpaces(startnum)+&sw
       endif

       " if this is the end of a comment block
       if cur =~ '^[! ]*\*/'
           " we want to indent the closing */ at the same level as the opening /*
           return CountLeadingSpaces(startnum) 
       endif

       " if we are inside a formal comment
       if getline(startnum) =~ '^\s*/\*\*'

            if cur =~ '<b>\(Ensures\|Requires\):</b>'
                return CountLeadingSpaces(startnum)+&sw 
            endif

            if prev =~ '^\s*<li>.*' && cur !~ '^\s*<li>.*' 
                if cur =~ '^\s*</ul><li>\s*else.*'
                    return prevcount - 5
                elseif cur !~ '^\s*</ul>\s*'
                    return prevcount + 5
                endif
            endif

            if cur =~ '^\s*<li>.*'
                if prev =~ '.*:\s*<ul>\s*$' && prev !~ '^\s*<li>'
                    return prevcount
                endif

                if prev =~ '^\s*<li>.*' || prev =~ '^\s*</ul>.*' || prev =~ '<b>\(Ensures\|Requires\):</b>'
                    if prev =~ '^\s*<li>\s*if\s*(' || prev =~ '^\s*</ul><li> else' || prev =~ '\s*<li>.*:\s*<ul>'
                        return prevcount + 5
                    elseif prev =~ '^\s*</ul>\s*'
                        return prevcount - 5
                    else
                        return prevcount 
                    endif
                else
                    return prevcount - 5
                endif
            endif

       endif
     
       return -1
    endif " end of formal comment formatting

    " if this is one of my // -------- type comments 
    if cur =~ '^\s*// -------*'
       return theIndent - &sw
    endif
    " if this is a normal // comment then just return the normal cindent
    " for it. 
    if cur =~ '^\s*//.*'
       return theIndent 
    endif

    " Don't indent after an annotation
    if prev =~ '^\s*@'
       return CountLeadingSpaces(v:lnum-1)
    endif

    return theIndent
endfunction

function! GetMyCppIndent()
    let theIndent = cindent(v:lnum)
    let cur = getline(v:lnum)
    let prev = getline(v:lnum-1)

    let curcount = CountLeadingSpaces(v:lnum)
    let prevcount = CountLeadingSpaces(v:lnum-1)

    " These lines are here to make vim indent lambda functions correctly.
    if (prev =~']\s*(.*)\s*{\s*$') && (cur =~ '^\s*}\s*$')
        return theIndent-&sw 
    endif
    if (cur =~ '^\s*}\s*)\s*;*\s*$')
        return theIndent-&sw 
    endif

    " Don't format comments unless they are my formal comments.  
    " Then format them but only how I say :)
    if InCppComment(v:lnum)
       " if this is the start of a formal comment block
       if cur =~ '^\s*/\*!'
          return theIndent 
       endif

       " if this is a /*    */  comment on a single line
       if cur =~ '^\s*/\*.\{-}\*/'
           return theIndent
       endif

       let startnum = FindCommentStart(v:lnum)
       let startcount = CountLeadingSpaces(startnum)

       if startnum == v:lnum-1 && cur =~ '^\s*$'
           return startcount+&sw
       endif

       " if this is the end of a comment block
       if cur =~ '^[! ]*\*/'
           " we want to indent the closing */ at the same level as the opening /*
           return startcount 
       endif

       " if we are inside a formal comment
       if getline(startnum) =~ '^\s*/\*!'
           if cur =~ '^\s*\(ensures\|requires\|throws\)\s*$'
               return startcount+&sw 
           endif
           if prev =~ '^\s*\(ensures\|requires\|throws\)\s*$'
               return prevcount+&sw 
           endif
           if prev =~ '^\s*$'
               return -1
           endif
           if prev =~# '^\s*[A-Z][A-Z0-9 _:\*]*\s*$'  
               return prevcount+&sw 
           endif
           if prev =~ '^\s*-' && cur !~ '^\s*-' && curcount != prevcount+&sw 
               return prevcount+2
           endif
           if cur =~ '^\s*-'
               if cur =~ '^\s*- else\s*$'
                   return (prevcount - &sw) - (prevcount - &sw)%&sw
               elseif curcount%&sw == 0
                   return -1
               elseif prev =~ '^\s*- else\s*$'
                   return prevcount + &sw
               elseif prev =~ '^\s*- if ('
                   return prevcount + &sw
               elseif prev =~ '^\s*-.*' 
                   return prevcount 
               elseif curcount%&sw != 0 
                   return curcount - curcount%&sw
               endif
               return -1
           endif
       endif

       return -1
   endif " end of formal comment formatting

    " if this line is just a {
    if cur =~ '^\s*{\s*$' && prev =~ 'class' 
        return prevcount 
    endif

    " if this line is just a >
    if cur =~ '^\s*>' 
        return prevcount 
    endif

    if prev =~ '^\s*template\s*<.*>\s*$' 
        return prevcount 
    endif

    if prev =~ '^\s*typename '
        return prevcount 
    endif

    if prev =~ '::\s*$'
        return prevcount 
    endif
    if prev =~ '^[^(]*,\s*$'
        return prevcount 
    endif

    if prev =~ '^\s*template \s*<\s*$'
        return prevcount + &sw
    elseif prev =~ '^\s*template <'
        return -1
    endif

    " if this is one of my // -------- type comments 
    if cur =~ '^\s*// -------*'
       return theIndent - &sw
    endif
    " if this is a normal // comment then just return the normal cindent
    " for it. 
    if cur =~ '^\s*//.*'
       return theIndent 
    endif

    if prev =~ '^\s*>'
        let theIndent = theIndent-&sw
        if theIndent < 1 
            let theIndent = 0
        endif
        return theIndent
    endif

    return theIndent
endfunction

function! GetMyXmlIndent()
    let cur = getline(v:lnum)
    let prev = getline(v:lnum-1)
    let opentag = '<[^!/>][^/>]*>'
    let closetag = '</[^>]*>'

    " if this line is a closing tag
    if cur =~ '^\s*</[^>]*>'
        let depth = 0
        let tagname = matchstr(cur,'</[^>]*')
        let tagname = matchstr(tagname,'[^ ]*',2)
        let opentag = '<' . tagname . '[^/>]*>'
        let closetag = '</' . tagname . '\s*>'
        let pos = v:lnum-1
        while (getline(pos) !~ opentag || depth != 0) && pos > 1
            if getline(pos) =~ closetag
                let depth = depth + 1
            elseif getline(pos) =~ opentag
                let depth = depth - 1
            endif
            let pos = pos - 1
        endwhile
        if pos == 0
            return -1
        else
            return CountLeadingSpaces(pos)
        endif
    elseif prev =~ opentag && prev !~ closetag
        return CountLeadingSpaces(v:lnum-1)+&sw
    else
        return CountLeadingSpaces(v:lnum-1)
    endif

endfunction

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" close the preview window if it was opened in insert mode (probably because
" of omnicompletion with the 'preview' option set in completeopt)
augroup closepreview
    " Detect if the preview window existed before entering insert mode.
    autocmd InsertEnter * let t:preview_open=IsPreviewWinOpen()

    " Close the preview window when exiting insert mode so that the
    " completion-menu "preview" option doesn't get in the way of editing.
    " But, don't close it if it was already open before insert mode, or if on
    " the command line (pclose is not allowed on the command line)
    autocmd InsertLeave *
                \ if !t:preview_open && bufname('') !~# (v:version < 702 ? 'command-line' : '\[Command Line\]') |
                \   pclose |
                \ endif
augroup END

function! IsPreviewWinOpen()
    let winnum=winnr('$')
    while winnum > 0
        if getwinvar(winnum, '&previewwindow')
            return 1
        endif
        let winnum -= 1
    endwhile
    return 0
endfunction

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Python select lines in visual mode and execute function 
"
" Execute currently selected visual range as Python.  Lines are pre-processed
" to remove extra indentation, leaders, or decorators that might be in place
" due to the line range being part of a code block in a markup-language
" document (such as ReStructured Text, Markdown, etc.)
" Usage: Select a range of line in the buffer and then call ':EvalPy' to
" execute those lines in the default system Python and show the results in the
" command window. Using the 'bang' operator (':EvalPy!') will execute the
" lines and insert the results in the current buffer.
function! <SID>EvaluateCurrentRangeAsMarkedUpPython(insert_results) range
    "" get lines
    let [lnum1, col1] = getpos("'<")[1:2]
    let [lnum2, col2] = getpos("'>")[1:2]
    let lines = getline(lnum1, lnum2)
    " let lines[-1] = lines[-1][: col2 - 2]
    " let lines[0] = lines[0][col1 - 1:]
 
    "" remove blank rows
    let rows = []
    for line in lines
        let row = substitute(line, '^\s*\(.\{-}\)\s*$', '\1', '')
        if len(row) > 0
            call add(rows, line)
        endif
    endfor
    let lines = rows
 
    if len(lines) == 0
        return
    endif
    let leader = matchstr(lines[0], '^\s*\(>>>\|\.\.\.\)\{0,1}\s*')
    let leader_len = len(leader)
    let code_lines = []
    for line in lines
        let code_line = strpart(line, leader_len)
        call add(code_lines, code_line)
    endfor
    let code = join(code_lines, "\n")
    if empty(a:insert_results)
        redir => result
        silent execute "!python -c " . shellescape(code)
        redir END
        let rows = split(result, '\n')[1:]
        let result = join(rows, "\n")
        echo result
    else
        let endpos = getpos("'>")
        call setpos('.', endpos)
        execute "r !python -c " . shellescape(code)
    endif
endfunction
command! -bang -range EvalPy :call s:EvaluateCurrentRangeAsMarkedUpPython("<bang>")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" My additions

"turn on line numbering
"set nu

"cursor line wrapping
"set whichwrap=<,>,h,l,[,]



"Key mappings for copy and paste
"vmap <C-c> "py
"nmap <C-c> "pyiw
"vmap <C-v> "pp
"nmap <C-v> "pP
"imap <C-v> <Esc>"ppa
"map <C-z> <Esc>
"imap <C-z> <Esc>ui

"Set backspace
"set backspace=indent,eol,start

"set term=builtin_ansi       " Make arrow and other keys work

"behave mswin

"if !exists("autocommands_loaded")
"    let autocommands_loaded = 1
"    autocmd BufRead,BufNewFile,FileReadPost *.py source ~/.vim/python
"endif

" Remember last line in previous file edit
"au BufReadPost * if line ("'\"") > 0|if line ("'\"") <= 
"   \line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

