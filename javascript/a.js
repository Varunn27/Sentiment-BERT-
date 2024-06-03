function initializeGraphs(pieChartData) {  
    console.log('initializeGraphs');
    var data = [{  
        values: pieChartData,  
        labels: ['Positive', 'Neutral', 'Negative'],  
        type: 'pie',  
        marker: {  
            colors: [  
                'rgba(75, 192, 192, 0.2)',  
                'rgba(54, 162, 235, 0.2)',  
                'rgba(255, 99, 132, 0.2)'  
            ],  
            line: {  
                color: [  
                    'rgba(75, 192, 192, 1)',  
                    'rgba(54, 162, 235, 1)',  
                    'rgba(255, 99, 132, 1)'  
                ],  
                width: 1  
            }  
        }  
    }];  
    console.log('data', data);  
    var layout = {  
        title: 'Sentiment Distribution',  
        showlegend: true  
    };  
  
    Plotly.newPlot('sentimentPieChart', data, layout);  
}  
