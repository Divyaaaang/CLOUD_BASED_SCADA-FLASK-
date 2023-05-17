var product1_data = [];
        var product2_data = [];
        var product3_data = [];

        // Define the time intervals for each set of data
        var product1_interval = 1000; // 1 second
        var product2_interval = 2000; // 2 seconds
        var product3_interval = 3000; // 3 seconds

        // Define the plot data traces for each product
        var trace1 = {
            x: [],
            y: [],
            name: 'Product 1',
            mode: 'lines'
        };
        var trace2 = {
            x: [],
            y: [],
            name: 'Product 2',
            mode: 'lines'
        };
        var trace3 = {
            x: [],
            y: [],
            name: 'Product 3',
            mode: 'lines'
        };

        // Define the plot layout options
        var layout = {
            title: 'Line Graph',
            xaxis: {
                title: 'Time'
            },
            yaxis: {
                title: 'Value'
            }
        };

        // Create the plot figure
        var plot = Plotly.newPlot('plot', [trace1, trace2, trace3], layout);

        // Update the plot data for each product at their respective time intervals
        setInterval(function() {
            // Update the data for Product 1
            var product1_value = Math.random() * 10;
            product1_data.push(product1_value);
            trace1.x.push(new Date());
            trace1.y.push(product1_value);
            Plotly.redraw('plot');

            // Update the data for Product 2
            if (trace2.x.length == 0 || new Date() - trace2.x[trace2.x.length - 1] >= product2_interval) {
                var product2_value = Math.random() * 10;
                product2_data.push(product2_value);
                trace2.x.push(new Date());
                trace2.y.push(product2_value);
                Plotly.redraw('plot');
            }

            // Update the data for Product 3
            if (trace3.x.length == 0 || new Date() - trace3.x[trace3.x.length - 1] >= product3_interval) {
                var product3_value = Math.random() * 10;
                product3_data.push(product3_value);
                trace3.x.push(new Date());
                trace3.y.push(product3_value);
                Plotly.redraw('plot');
            }
        }, 1000); // Update the plot data every second
 