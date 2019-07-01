
set terminal pngcairo enhanced color lw 1 size 1000, 700 font 'Arial-Bold'
set output "inflight_tcp.png"

set ylabel "Inflight (bytes)" font ",18"
set key outside horizontal;
#set key right top;

set style fill solid 0.25 border 2
set style boxplot nooutliers pointtype 7
set style data boxplot
#set boxwidth 0.5
#set pointsize 0.5

set xtics ("100Mb/s" 2, "1000Mb/s" 6) scale 0.0
set xtics nomirror
#set ytics nomirror
set title 'Bytes in flight comparison for TCP'

#set yrange [0:160000]

plot "fdemu_100_tcp.plotme" using (1):2 lc rgb "red" title "FdEmu", \
	 "netmap_100_tcp.plotme" using (2):2 lc rgb "green" title "Netmap", \
	 "dpdk_100_tcp.plotme" using (3):2 index 0 lc rgb 'blue' title "dpdk",\
	 "dpdk_1000_tcp.plotme" using (5):2 index 0 lc rgb 'blue' notitle,\
	 "netmap_1000_tcp.plotme" using (6):2 lc rgb 'green' notitle, \
	 "fdemu_1000_tcp.plotme" using (7):2 lc rgb 'red' notitle 
