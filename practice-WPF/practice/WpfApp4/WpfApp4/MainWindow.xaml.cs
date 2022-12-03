using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
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

namespace WpfApp4
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private ObservableCollection<Customer> _customers = new ObservableCollection<Customer>(); 
        private int _index = 0; public MainWindow()
        {
            InitializeComponent();

            _customers.Add(new Customer { Id = ++_index, Name = "name" + _index, Phone = "phone" + _index });
            _customers.Add(new Customer { Id = ++_index, Name = "name" + _index, Phone = "phone" + _index });
            _customers.Add(new Customer { Id = ++_index, Name = "name" + _index, Phone = "phone" + _index });
            CustomerListView.ItemsSource = _customers;
        }

        private void AddButton_Click(object sender, RoutedEventArgs e)
        {
            _customers.Add(new Customer { Id = ++_index, Name = "name" + _index, Phone = "phone" + _index });
            CustomerListView.ItemsSource = _customers;

        }

        private void SearchTextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            var filterList =
                _customers.Where(x => x.Name.Contains(SearchTextBox.Text)).ToList(); 
                CustomerListView.ItemsSource = filterList;

        }
    }
}

