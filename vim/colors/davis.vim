" Vim color file
" Maintainer:	Hans Fugal <hans@fugal.net>
" Last Change:	$Date: 2003/07/24 00:57:11 $
" Last Change:	$Date: 2003/07/24 00:57:11 $
" URL:		http://hans.fugal.net/vim/colors/desert.vim
" Version:	$Id: desert.vim,v 1.7 2003/07/24 00:57:11 fugalh Exp $





hi clear
set background=light
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "davis"




hi Todo		guifg=orangered guibg=yellow2
hi StatusLine ctermfg=11 ctermbg=12 cterm=none guifg=#ffffff guibg=#555555 gui=none
hi Directory  ctermfg=2						  guifg=#006600 gui=bold




""""""" Black
hi Normal	        guifg=Black guibg=White ctermbg=White ctermfg=Black
hi cCurleyBracket	guifg=black gui=bold 
hi cEllipsesError	guifg=Black ctermfg=Black
hi Identifier	    	guifg=Black ctermfg=black
hi Operator	        guifg=Black ctermfg=black
hi cUserLabel	    	guifg=Black ctermfg=black
hi Cursor	        guibg=black guifg=white
hi xmlComment       	guifg=Black ctermfg=Black 
hi xmlAttrib        	guifg=Black ctermfg=Black 
hi makeSpecial	   	guifg=Black ctermfg=Black 
hi cppIncludeFile  	guifg=Black ctermfg=Black 


""""""" DarkBlue
hi Type	    		guifg=#3333ff gui=underline  ctermfg=DarkBlue  cterm=underline
hi Statement	        guifg=#3333ff gui=NONE ctermfg=DarkBlue 
hi cSizeofOperator	        guifg=#3333ff gui=NONE ctermfg=DarkBlue 
hi xmlTagName	   	guifg=#3333ff ctermfg=DarkBlue 
hi xmlTag	      	guifg=#3333ff ctermfg=DarkBlue 
hi xmlEndTag	   	guifg=#3333ff ctermfg=DarkBlue 
hi makeComment	   	guifg=#3333ff ctermfg=DarkBlue 


""""""" DarkGreen
hi Comment	        guifg=#009900 ctermfg=DarkGreen
hi xmlAttribPunct   	guifg=#009900 ctermfg=DarkGreen 
hi xmlCommentPart   	guifg=#009900 ctermfg=DarkGreen 


""""""" DarkCyan

""""""" DarkRed
hi xslElement	    	guifg=#009900 ctermfg=DarkRed
hi String	        guifg=#dd0000 ctermfg=DarkRed
hi cString	        guifg=#dd0000 ctermfg=DarkRed
hi cCharacter	    	guifg=#dd0000 ctermfg=DarkRed


""""""" DarkMagenta
hi Function	        guifg=#bb00bb  ctermfg=DarkMagenta 


""""""" DarkYellow
hi cPreCondit       	ctermfg=DarkYellow  guifg=DarkYellow
hi cPreProc         	ctermfg=DarkYellow  guifg=DarkYellow
hi cDefine          	ctermfg=DarkYellow  guifg=DarkYellow
hi cInclude         	ctermfg=DarkYellow  guifg=DarkYellow
hi cMacro           	ctermfg=DarkYellow  guifg=DarkYellow


""""""" LightGray
hi cEscapeChar		guifg=#bbbbbb ctermfg=LightGray  


""""""" DarkGray
hi Number	        guifg=#606060 ctermfg=DarkGray
hi cOctal	        guifg=#606060 ctermfg=DarkGray
hi cOctalZero	    	guifg=#606060 ctermfg=DarkGray
hi cppBoolean	    	guifg=#606060 ctermfg=DarkGray
hi c99Boolean	    	guifg=#606060 ctermfg=DarkGray
hi LineNr	        guifg=#606060 ctermfg=DarkGray
hi xmlString       	guifg=#606060 ctermfg=DarkGray 


""""""" Blue
hi cMathOperator	guifg=#ce9100 ctermfg=Blue
hi cLogicalOperator	guifg=#ce9100 ctermfg=Blue
hi cBinaryOperator	guifg=#ce9100 ctermfg=Blue


""""""" Green
""""""" Cyan
""""""" Red


""""""" Magenta
""""""" Yellow








