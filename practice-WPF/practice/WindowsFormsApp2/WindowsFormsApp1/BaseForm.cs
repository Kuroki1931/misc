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
    public partial class BaseForm : Form
    {
        public BaseForm()
        {
            InitializeComponent();
            this.toolStripProgressBar1.Maximum = 100;
            this.toolStripProgressBar1.Minimum = 0;
            this.toolStripStatusLabel1.Text = "";

        }

        protected void SetStatusLabel(string message)
        {
            this.toolStripStatusLabel1.Text = message;
        }
        protected void SetProgress(int value)
        {
            this.toolStripProgressBar1.Value = value;
        }
    }
}
