using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void ShowButton_Click(object sender, EventArgs e)
        {
            var val = GetAmount();
            ShowLabel.Text = (val * 1.08m).ToString();

        }

        private decimal GetAmount()
        {
            return 100m;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var money = new Money(GetAmount());
            ShowLabel.Text =  money.TaxValue + "円";
        }
    }
}
