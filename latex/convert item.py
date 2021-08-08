with open('convert_input.txt', 'r', encoding='utf8') as fi:
    with open('convert_output.txt', 'w', encoding='utf8') as fo:
        s = '\\begin{itemize}'
        for line in fi:
            if '-' in line:
                line = line[line.find('-'):]
                line = line.strip()
                s += '\n' + '\item' + line.strip('-') 
            else:
                s += ' ' + line
        s += '\\end{itemize}'
        fo.write(s)

'''
\setsansfont[SizeFeatures={Size=14}]{Times New Roman}
\setmonofont[SizeFeatures={Size=14}]{Times New Roman}
\fontspec[SizeFeatures={Size=14}]{Times New Roman}
\defaultfontfeatures{SizeFeatures={Size=14}}
\addfontfeatures{SizeFeatures={Size=14}}

\renewcommand{\baselinestretch}{1.75}

\makeatletter
\renewcommand\normalsize{%
	\@setfontsize\normalsize{14pt}{14pt}% Will look incredibly crabbed if line height is too small
	\abovedisplayskip 10\p@ \@plus2\p@ \@minus5\p@%
	\abovedisplayshortskip \z@ \@plus2\p@%
	\belowdisplayshortskip 5\p@ \@plus2\p@ \@minus3\p@%
	\belowdisplayskip \abovedisplayskip%
	\let\@listi\@listI%
}
\normalsize  
\makeatother
'''