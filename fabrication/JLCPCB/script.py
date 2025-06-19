#!/usr/bin/env python3
import os
import csv
import sys

def main():
    # Get directory from command line argument or user input
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory name (e.g., 'gerbers', 'gerbers-v0.2'): ").strip()
    
    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found")
        return
    
    # Get all files in the directory
    files = os.listdir(directory)
    
    # Find csv files
    csv_files = [f for f in files if f.endswith('.csv')]
    
    if len(csv_files) < 3:
        print(f"Error: Expected at least 3 CSV files, but found {len(csv_files)}")
        return
    
    # Identify position files and project file
    top_pos_file = None
    bottom_pos_file = None
    bom_file = None
    
    for file in csv_files:
        if file.endswith('-top-pos.csv'):
            top_pos_file = file
        elif file.endswith('-bottom-pos.csv'):
            bottom_pos_file = file
        elif not (file.endswith('-pos.csv') or file.startswith('BOM_') or file.startswith('CPL_')):
            bom_file = file
    
    # Verify necessary files were found
    if not top_pos_file:
        print("Error: Top position file not found")
        return
    
    if not bottom_pos_file:
        print("Error: Bottom position file not found")
        return
    
    if not bom_file:
        print("Error: BOM file not found")
        return
    
    print(f"Found files:")
    print(f"- Top CPL: {top_pos_file}")
    print(f"- Bottom CPL: {bottom_pos_file}")
    print(f"- BOM file: {bom_file}")
    
    # Process position files - change headers
    position_files = [top_pos_file, bottom_pos_file]
    for pos_file in position_files:
        # Read the file
        rows = []
        with open(os.path.join(directory, pos_file), 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            
            # Verify header format
            if header != ['Ref', 'Val', 'Package', 'PosX', 'PosY', 'Rot', 'Side']:
                print(f"Warning: Unexpected header format in {pos_file}")
                print(f"Expected: Ref,Val,Package,PosX,PosY,Rot,Side")
                print(f"Found: {','.join(header)}")
            
            # Create new header
            new_header = ['Designator', 'Val', 'Package', 'Mid X', 'Mid Y', 'Rotation', 'Layer']
            
            # Add the new header and all data rows
            rows.append(new_header)
            for row in reader:
                rows.append(row)
        
        # Write the modified file
        with open(os.path.join(directory, pos_file), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        
        print(f"Updated headers in {pos_file}")
    
    # Rename position files
    new_top_pos_file = f"CPL_{top_pos_file}"
    new_bottom_pos_file = f"CPL_{bottom_pos_file}"
    
    os.rename(os.path.join(directory, top_pos_file), os.path.join(directory, new_top_pos_file))
    os.rename(os.path.join(directory, bottom_pos_file), os.path.join(directory, new_bottom_pos_file))
    
    print(f"Renamed {top_pos_file} to {new_top_pos_file}")
    print(f"Renamed {bottom_pos_file} to {new_bottom_pos_file}")
    
    # Rename project file
    new_project_file = f"BOM_{bom_file}"
    os.rename(os.path.join(directory, bom_file), os.path.join(directory, new_project_file))
    print(f"Renamed {bom_file} to {new_project_file}")
    
    print("All operations completed successfully!")

if __name__ == "__main__":
    main()