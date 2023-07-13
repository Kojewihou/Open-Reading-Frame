import matplotlib.pyplot as plt

# No Local Imports

def PlotORFs(sequence, ORFs):

    sequence_length = len(sequence)

    # Initialise blank plot
    fig, ax = plt.subplots(3,1, figsize=(9,5))

    # Set a blank plot for each frameshift running the length of the sequence
    for i in range(3):
        #Format plots
        ax[i].get_yaxis().set_ticks([])
        ax[i].set_ylabel("RF "+ str(i+1), rotation= 0, labelpad=20, style= "oblique")
        ax[i].get_xaxis().set_visible(False)    
        ax[i].set_xlim(0,sequence_length)
        ax[i].set_ylim(0,30)
        ax[i].axhline(y=15.3, color= "goldenrod", linewidth= 2)
        ax[i].axhline(y=14.7, color= "cornflowerblue", linewidth= 2)
        ax[i].text(sequence_length, 0.6*30, "  forward", va="center", ha="left", style="italic",size="smaller", color="goldenrod")
        
        ax[i].text(sequence_length, 0.4*30, "  reverse", va="center", ha="left", style="italic",size="smaller", color="cornflowerblue")
    ax[2].get_xaxis().set_visible(True)
    ax[2].set_xlabel("Sequence Length:" + str(sequence_length))

    # Add reads to the plot
    for read in ORFs:
        if not read.reversed:
            ax[read.frame].axvline(x= read.start, color= "g", linestyle= "solid", ymin= 0.5, ymax = 0.9)
            ax[read.frame].axvline(x= read.end, color= "r", linestyle= "solid", ymin= 0.5, ymax = 0.9)
            ax[read.frame].arrow(read.start,30*0.8, read.length, 0, color= "black", length_includes_head= True, head_width=1, head_length=10, linestyle="dotted")
        else:
            ax[read.frame].axvline(x= sequence_length - read.start, color= "g", linestyle= "solid", ymin= 0.5, ymax = 0.1)
            ax[read.frame].axvline(x= sequence_length - read.end, color= "r", linestyle= "solid", ymin= 0.5, ymax = 0.1)
            ax[read.frame].arrow(sequence_length - read.start,30*0.2, -read.length, 0, color= "black", length_includes_head= True, head_width=1, head_length=10, linestyle="dotted")
            
    plt.show()

