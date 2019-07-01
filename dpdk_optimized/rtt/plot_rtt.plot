#set xrange [0:30]
set terminal pngcairo enhanced color lw 1 size 1000, 700 font 'Arial-Bold'
set output "tcp_rtt_0.png"

#set xlabel "Time (Seconds)" font ",18"
set ylabel "RTT (secs, logscale)" font ",18"
#set key vertical maxrows 1
set style fill solid 0.25 
set style boxplot nooutliers pointtype 7
set style data boxplot
set format y '%g'
set xtics ("100 Mbps" 2, "1000 Mbps" 6)
set xtics nomirror
set ytics nomirror
set title 'RTT comparison for TCP'
set logscale y 2
set yrange [:1]
	 
plot "fdemu_100mbps.txt" using (1):1 lc rgb 'red' title "FdEmu",\
	 "netmap_100mbps.txt" using (2):1 lc rgb 'green' title "Netmap", \
	 "dpdk_100mbps.txt" using (3):1 lc rgb 'blue' title "Dpdk", \
	 "dpdk_1000mbps.txt" using (5):1 lc rgb 'blue' notitle, \
	 "netmap_1000mbps.txt" using (6):1 lc rgb 'green' notitle,\
	 "fdemu_1000mbps.txt" using (7):1 lc rgb 'red' notitle 
