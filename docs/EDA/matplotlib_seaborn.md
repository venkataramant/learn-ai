# ****************************************
# Visualization

# Graphs
   Histogram
      - Tallest clusters of bars -- indicates modes
      - Left/Negative skewed (If less number of points on left side)
      - Right/Positive Skewed (If less number of points on rights side)
   BarGram
   Pie

# Matplotlib.Pyplot

     from matplotlib import pyplot
## Plots from pyplot
    1. subplot
    2. boxplot

## Graph Methods
        scatter(x,y,color,size,marker,alpha)
        
        linechart(x,y,linestyle,c,lw)
                "r--"
        bar(X,Y,color,align(edge/centre),width,edgecolor,lw=6)
     
        hist(ages,bins=4/[10 20 50 70], cumulative)
     
        pie(votes,labels=langs)
        legend(bbox_to_anchor=[])

## Methods
    xlabel()
    xlim()
    xticks(rotation=90)
    ylabel()
    ylim()
    title()
    figure(figsize=(x,y))
    show()
    tight_layout()
## Display
         show()
         xtricks()
            rotation=Number
         title()
         xlabel()
         ylabel()
         xlim()
         ylim()
   

# Seaborn

##    Quantitative / Numerical Variable

    Univariate Analysis – Analysing one variable

    displot() – Visualize the distribution of variable (also called histogram)
    boxplot() or violinplot() - To check specifically for outliers
##    Bivariate Analysis – Relationship between 2 variables

    jointplot() or pairplot()
    lmplot() – Scatter plot with a best fit line

##    Multivariate Analysis – Relationship between more than 2 variables

    corr() – Correlation matrix followed by
    heatmap() – Visualize the correlation matrix
    pairplot() – Combination of Scatter plots and individual histogram plots for all numerical
    variables in the dataset. Also, can assign a categorical variable using hue as an add on)

##    Qualitative/ Categorical Variables

    Univariate Analysis – Analysing one variable

    countplot() – Visualize the distributions of categorical variable
##    Quantitative vs Qualitative Variables

    Analyse how a quantitative variable varies across categorical variable(s)

    boxplot() or violinplot() – To check specifically for outliers
    stripplot() or swarmplot() – Scatter plot across a categorical variable (also helps in checking for outliers)
    barplot() – Can also create a clustered bar chart (assign a categorical variable to hue) or a stacked bar chart (2 bar plots with different colors)
    pointplot()
    lineplot() – Best when looking at trends (Time-related variable along the x-axis)
    catplot() or factorplot() – Analysing a quantitative variable across 2 categorical variables with
    one variable having a high number of categories

 ## Plots
        Relation (relplot)
            scatterplot,lineplot (2)
        Distributions (distplot)
            histplot,kdeplot,ecdfplot,rugplot (4)
            countplot
        Categorical (catplot)
            striplot/swamplot/boxplot/violinplot/pointplot/barplot (6)
            boxenplot
        Linear/Regression
            lmplot/regplot/residplot
        Others
            joinplot/pairplot

        01. barplot 
            A bar plot represents an aggregate or statistical estimate for a numeric variable with the height of each rectangle and indicates the uncertainty around that estimate using an error bar.
        02. boxplot/boxenplot
            - also known as whisker plot (5 number visuliazation)
            [data,x,y,color,showfliers]
            boxenplot - creates different levels in the box to represent density
        03. catplot
            -categorical plot
            - shows average with 95% line
            [data,x,y,hue,col,kind,jitter=True]

            kind=[bar ->histo like
                  count  -> same as countplot,
                  box -> boxplot
                  violin -> more gentle than box
                  boxen 
                  strip/swarm
                  point (line)]
        04. countplot
            - A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable. 
            - Counts how many times a 'value' is repeated
            [data,x,hue]

        05. displot/distplot
            - single line, a figure-level function 
            [data,kind]
            kind=[kde/hist/ecdf]
       
            
        07. histplot
            - X represents ranges/bins
            - Y represents no of rows belongs each of those ranges/bins
            [data,x,color,bins,stat,kde,hue]
            kde -> line shows trend of "x" values
            bins=integer formula::->[Range/binwidth]
            binwidth formula::->[2*IQR]/sqrt(n)**3
            stat=[density/]
            kde=Boolean
            hue
        10. lineplot/kdeplot
            [data,x,y,ci,hue,style,markers,err_style]
            ci=True/False - confidence intervals.
            err_style=[bands/bars] 
        08. jointplot
            scatterplot+histoplot of (x,y)
            [data,x,y,kind,fill]
            
            kind ["scatter", "hist", "hex", "kde", "reg", "resid"]
                    hex - hexagonal (coloring of scatter)
                    reg - regression(line of best fit)
                    kde - kernel density estimator
                    hist - histogram
                    resid - residual
            
  
        11. lmplot/regplot/residplot
                linearModel Plot,regression plot,residual plot
                all 3 are related to standard deviation/regression.
                all 3 uses scatter style. residplot - scatter represents residual(difference between actual and estimated values)
                Line of Best fit with scatter plot
                [data,x,y,hue,col,height,aspect,lowes(residplot)]
                hue/col -(different color/plot)
                lowes(residplot)
        12. miscplot
        13. palplot
        14. pointplot
        16. relplot
            - Multiple plots either scotter/boxplots
            [data,x,y,col,kind='line',ci=None,col_wrap=4,hue]

        18. scatterplot
            - provides points (x,y)
            - provides strong/weak correlation (positive/negative/NO)
            data,x ,y,hue,style (column_names)
        19. stripplot/swamplot
            scatter values in  boxplot style
            data,x,y,jitter,hue
            swamplot is like striplot with more organized data visualization
            dodge=True
        20. violinplot
            boxplot + kde
            univariable analysis
            data,x,y,orient='v'
            if (both x and y are given y is used for frequence and for each in x  one violin is drawn.)
        21. subplots
        22. heatmap 
             - create plot for .corr() result
             - for a given variables set and their correlation it depicts as grap.
             data=df[["c1","c2,"c3"]].corr()
             [.corr(),annot,cbar,cmap]

        23. pairplot (multiple scatter plots for given n variables)
 ##     palettes
        
        color_palette/choose_colorbrewer_palette
        blend_palette
        crayon_palette
        cubehelix_palette/choose_cubehelix_palette
        dark_palette/choose_dark_palette
        hls_palette
        husl_palette
        light_palette/choose_light_palette
        mpl_palette
        xkcd_palette
        choose_diverging_palette
# Grids

    - Separate Graphs
    'FacetGrid'
        - Similar to Hue
    'JointGrid',
    'PairGrid',
# Styles
    axes_sytle('whitegrid')     

## Methods


# *************** How To Handle Missing Data *********************


    1. Drop the rows
    2. Drop the column
    3. Imputation - Update Missing values
        1. Mean/Mode/Median
        2. Group by relevant categories.
    4. Predictive Modelling


# Skewed


# Definitions
## Central Tendeny
## Mean
## Median
## Mode
## Standard Deviation
## KDE/ECDF
    - Kernel Density Estimation
    - Empirical cumulative distribution function
## Dispersion
## Correlation
## Regression
## IQR
## Outliers
    > 1.5 of IQR (left and right)

## Bimodal distribution
## Skeweds
## confidence interval
## MCAR 
     - Missing completely At Random
## Anomaly Detection algorithms
    - Isolation forest
    - One-class SVM
    - Autoencoders
## Sparsity 
    - is a noun that means something is scattered or scanty, and lacks density.
## N-Gram Model
## Document Term Matrix
## lmplot 
# Cleaing Text
    1. Stop Words
        - the,an,in
    2. Stemming
        - Returning words to their original stem.
        chopping/chopped -? Chop
    3. Lower case/Remove [Punctuations, extra white space,numbers]
