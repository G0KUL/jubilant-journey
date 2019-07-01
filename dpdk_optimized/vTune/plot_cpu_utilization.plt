set terminal pngcairo enhanced font "arial,10" fontscale 1.0 size 800, 600 
set output 'cpu utilization.png'
set boxwidth 0 absolute
set style fill solid 1.00 border lt -1
set key right top horizontal #Right noreverse noenhanced autotitle nobox
set style increment default

set ylabel "CPU Utilization (%)" font ",18"
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror #rotate by -45  autojustify
set xtics norangelimit 
set xtics ("TCP 100Mbps" 0, "UDP 100Mbps" 1, "TCP 100Mbps" 2, "UDP 1000Mbps" 3) scale 0.0
set title "Total CPU utilization" 

#set xrange [ * : * ] noreverse writeback
#set x2range [ * : * ] noreverse writeback
set yrange [ 0 : 50] noreverse writeback

plot 'data.dat' using 1 title "Fdemu", '' using 2 title "Netmap", '' using 3 title "Dpdk"
