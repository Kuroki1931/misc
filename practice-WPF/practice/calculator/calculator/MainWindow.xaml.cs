using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace calculator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public static Boolean cross = true;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Canvas_MouseDown(object sender, MouseButtonEventArgs e)
        {
            Canvas cnv = (Canvas)sender;
            if (cross)
            {
                int padding = 15;

                Line ln = new Line();
                ln.X1 = padding;
                ln.Y1 = padding;
                ln.X2 = cnv.Width - padding;
                ln.Y2 = cnv.Height - padding;
                ln.Stroke = Brushes.Blue;
                ln.StrokeThickness = 10;
                cnv.Children.Add(ln);
                Line ln2 = new Line();
                ln2.X1 = padding;
                ln2.Y1 = cnv.Height - padding;
                ln2.X2 = cnv.Width - padding;
                ln2.Y2 = padding;
                ln2.Stroke = Brushes.Blue;
                ln2.StrokeThickness = 10;
                cnv.Children.Add(ln2);
            }
            else
            {
                Ellipse el = new Ellipse();
                el.Width = 80;
                el.Height = 80;
                el.Margin = new Thickness(10, 10, 10, 10);
                el.Fill = Brushes.Transparent;
                el.Stroke = Brushes.Red;
                el.StrokeThickness = 10;
                cnv.Children.Add(el);
            }

            cross = !cross;
        }


    }
}
