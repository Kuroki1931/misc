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
    public partial class Form1 : BaseForm
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Class2 c2 = new Class2();
            MessageBox.Show(c2.GetAAA().ToString());
        }

        private void textBox1_Leave(object sender, EventArgs e)
        {
            int value = 0;
            if(!int.TryParse(textBox1.Text, out value))
            {
                textBox1.Text = "0";
            }
        }

    }
}
